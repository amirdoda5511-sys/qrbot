# bot.py
import asyncio
import io
import json
import logging
import re
import sys
from html import escape

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import qrcode
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import (
    Message,
    BufferedInputFile,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest

from config import BOT_TOKEN
import database
import locales

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
BOT_USERNAME = None  # Dinamik tarzda olinadi


def parse_url(text: str) -> str:
    """Matn ichidan barcha turdagi veb-sayt yoki video havolalarini topadi va to'g'ri HTTPS URL ga keltiradi."""
    text = text.strip()
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9.-]+\.(?:com|org|net|io|me|uz|ru|co|tv|app|site|dev|info|cc|bz|link|online|store|live)(?:/[^\s]*)?)'
    match = re.search(url_pattern, text, re.IGNORECASE)

    if match:
        url = match.group(0)
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        return url
    return None


async def get_direct_file_url(file_id: str) -> str:
    """Telegram serveridagi fayl/video uchun bir bosishda ochiladigan to'g'ridan-to'g'ri HTTPS havolani oladi."""
    try:
        file_info = await bot.get_file(file_id)
        if file_info and file_info.file_path:
            return f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"
    except Exception as e:
        logging.warning(f"Direct file URL olinmadi (file_id: {file_id}): {e}")
    return None


def get_language_keyboard():
    """Tilni tanlash uchun inline klaviaturani qaytaradi."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="set_lang:uz"),
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_lang:ru"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧 English", callback_data="set_lang:en"),
            ]
        ]
    )


def get_main_keyboard(lang: str):
    """Asosiy menyu uchun inline klaviatura."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=locales.get_text(lang, "btn_change_lang"),
                    callback_data="choose_lang"
                )
            ]
        ]
    )


def generate_qr(data: str) -> io.BytesIO:
    """Berilgan matn yoki to'g'ridan-to'g'ri havoladan QR-kod rasm generatsiya qiladi va BytesIO qaytaradi."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


async def process_and_send_qr(
    message: Message,
    media_type: str,
    data_to_encode: str,
    caption_preview: str = None
):
    """QR-kod generatsiya qilish va foydalanuvchiga yuborish uchun umumiy yordamchi funksiya."""
    user_id = message.from_user.id
    lang = database.get_user_language(user_id) or "uz"
    title_translated = locales.get_type_title(lang, media_type)

    processing_msg = await message.answer(locales.get_text(lang, "qr_processing"))
    try:
        qr_buffer = generate_qr(data_to_encode)
        photo = BufferedInputFile(qr_buffer.read(), filename="qrcode.png")

        ready_title = locales.get_text(lang, "qr_ready", title=title_translated)
        caption_text = f"{ready_title}\n\n"

        if caption_preview:
            short_preview = escape(
                caption_preview if len(caption_preview) <= 150 else caption_preview[:150] + "..."
            )
            caption_text += f"ℹ️ <i>{short_preview}</i>\n\n"

        caption_text += (
            f"{locales.get_text(lang, 'qr_link', link=escape(data_to_encode))}\n\n"
            f"{locales.get_text(lang, 'qr_scan_info', title=title_translated.lower())}"
        )

        await message.answer_photo(
            photo=photo,
            caption=caption_text,
            parse_mode=ParseMode.HTML,
            reply_markup=get_main_keyboard(lang)
        )
    except Exception as e:
        logging.error(f"QR generatsiyasida xatolik ({media_type}): {e}", exc_info=True)
        await message.answer(locales.get_text(lang, "error_gen"))
    finally:
        try:
            await processing_msg.delete()
        except Exception:
            pass


@dp.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    user_id = message.from_user.id
    args = command.args

    if args:
        # Deep link orqali kelgan foydalanuvchiga saqlangan media obyektini ko'rsatish
        media = database.get_media(args)
        lang = database.get_user_language(user_id) or "uz"

        if not media:
            await message.answer(locales.get_text(lang, "media_not_found"))
            return

        m_type = media["media_type"]
        file_id = media["file_id"]
        caption = media["caption"]
        extra = media["extra_data"]

        try:
            if m_type == "photo":
                await message.answer_photo(photo=file_id, caption=caption)
            elif m_type == "video":
                await message.answer_video(video=file_id, caption=caption)
            elif m_type == "document":
                await message.answer_document(document=file_id, caption=caption)
            elif m_type == "sticker":
                await message.answer_sticker(sticker=file_id)
            elif m_type == "audio":
                await message.answer_audio(audio=file_id, caption=caption)
            elif m_type == "voice":
                await message.answer_voice(voice=file_id, caption=caption)
            elif m_type == "animation":
                await message.answer_animation(animation=file_id, caption=caption)
            elif m_type == "video_note":
                await message.answer_video_note(video_note=file_id)
            elif m_type == "contact" and extra:
                c_data = json.loads(extra)
                await message.answer_contact(
                    phone_number=c_data.get("phone_number"),
                    first_name=c_data.get("first_name", ""),
                    last_name=c_data.get("last_name", "")
                )
            elif m_type == "location" and extra:
                l_data = json.loads(extra)
                await message.answer_location(
                    latitude=l_data.get("latitude"),
                    longitude=l_data.get("longitude")
                )
            elif m_type == "text":
                await message.answer(f"📄 <b>QR:</b>\n\n{escape(caption)}", parse_mode=ParseMode.HTML)
            else:
                await message.answer("⚠️ Media error.")
        except Exception as e:
            logging.error(f"Deep link media yuborishda xatolik ({m_type}): {e}", exc_info=True)
            await message.answer(locales.get_text(lang, "error_gen"))
        return

    # Oddiy /start - Til tanlanganligini tekshirish
    lang = database.get_user_language(user_id)
    if not lang:
        await message.answer(
            locales.TEXTS["uz"]["select_language"],
            reply_markup=get_language_keyboard(),
            parse_mode=ParseMode.HTML
        )
    else:
        await message.answer(
            locales.get_text(lang, "welcome"),
            reply_markup=get_main_keyboard(lang),
            parse_mode=ParseMode.HTML
        )


@dp.message(Command("lang"))
@dp.message(Command("language"))
async def cmd_language(message: Message):
    user_id = message.from_user.id
    lang = database.get_user_language(user_id) or "uz"
    await message.answer(
        locales.get_text(lang, "select_language"),
        reply_markup=get_language_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    user_id = message.from_user.id
    lang = database.get_user_language(user_id) or "uz"
    await message.answer(
        locales.get_text(lang, "help"),
        reply_markup=get_main_keyboard(lang),
        parse_mode=ParseMode.HTML
    )


@dp.callback_query(F.data == "choose_lang")
async def cb_choose_lang(callback: CallbackQuery):
    user_id = callback.from_user.id
    lang = database.get_user_language(user_id) or "uz"
    await callback.message.answer(
        locales.get_text(lang, "select_language"),
        reply_markup=get_language_keyboard(),
        parse_mode=ParseMode.HTML
    )
    try:
        await callback.answer()
    except TelegramBadRequest:
        pass


@dp.callback_query(F.data.startswith("set_lang:"))
async def cb_set_lang(callback: CallbackQuery):
    lang_code = callback.data.split(":")[1]
    user_id = callback.from_user.id

    database.set_user_language(user_id, lang_code)

    try:
        await callback.answer(locales.get_text(lang_code, "lang_changed"))
    except TelegramBadRequest:
        pass

    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer(
        f"{locales.get_text(lang_code, 'lang_changed')}\n\n"
        f"{locales.get_text(lang_code, 'welcome')}",
        reply_markup=get_main_keyboard(lang_code),
        parse_mode=ParseMode.HTML
    )


# Rasm (Photo)
@dp.message(F.photo)
async def handle_photo(message: Message):
    photo_file_id = message.photo[-1].file_id
    caption = message.caption or ""
    item_id = database.save_media("photo", file_id=photo_file_id, caption=caption)

    direct_url = await get_direct_file_url(photo_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "photo", direct_url, caption)


# Video
@dp.message(F.video)
async def handle_video(message: Message):
    video_file_id = message.video.file_id
    caption = message.caption or ""
    item_id = database.save_media("video", file_id=video_file_id, caption=caption)

    direct_url = await get_direct_file_url(video_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "video", direct_url, caption)


# Fayl / Hujjat (Document)
@dp.message(F.document)
async def handle_document(message: Message):
    doc_file_id = message.document.file_id
    file_name = message.document.file_name or "File"
    caption = message.caption or f"{file_name}"
    item_id = database.save_media("document", file_id=doc_file_id, caption=caption)

    direct_url = await get_direct_file_url(doc_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "document", direct_url, caption)


# Stiker (Sticker)
@dp.message(F.sticker)
async def handle_sticker(message: Message):
    sticker_file_id = message.sticker.file_id
    item_id = database.save_media("sticker", file_id=sticker_file_id)

    direct_url = await get_direct_file_url(sticker_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "sticker", direct_url)


# Audio / Musiqa
@dp.message(F.audio)
async def handle_audio(message: Message):
    audio_file_id = message.audio.file_id
    title = message.audio.title or "Audio"
    performer = message.audio.performer or ""
    caption = message.caption or f"{performer} - {title}".strip(" -")
    item_id = database.save_media("audio", file_id=audio_file_id, caption=caption)

    direct_url = await get_direct_file_url(audio_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "audio", direct_url, caption)


# Ovozli xabar (Voice)
@dp.message(F.voice)
async def handle_voice(message: Message):
    voice_file_id = message.voice.file_id
    item_id = database.save_media("voice", file_id=voice_file_id)

    direct_url = await get_direct_file_url(voice_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "voice", direct_url)


# Video xabar (Video note)
@dp.message(F.video_note)
async def handle_video_note(message: Message):
    vn_file_id = message.video_note.file_id
    item_id = database.save_media("video_note", file_id=vn_file_id)

    direct_url = await get_direct_file_url(vn_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "video_note", direct_url)


# Animatsiya / GIF
@dp.message(F.animation)
async def handle_animation(message: Message):
    anim_file_id = message.animation.file_id
    caption = message.caption or ""
    item_id = database.save_media("animation", file_id=anim_file_id, caption=caption)

    direct_url = await get_direct_file_url(anim_file_id)
    if not direct_url:
        direct_url = f"https://t.me/{BOT_USERNAME}?start={item_id}"

    await process_and_send_qr(message, "animation", direct_url, caption)


# Kontakt (Contact)
@dp.message(F.contact)
async def handle_contact(message: Message):
    contact = message.contact
    extra_data = json.dumps({
        "phone_number": contact.phone_number,
        "first_name": contact.first_name,
        "last_name": contact.last_name or ""
    })
    caption = f"{contact.first_name} ({contact.phone_number})"
    item_id = database.save_media("contact", extra_data=extra_data, caption=caption)

    # Directly format phone link (tel:) or deep link
    phone_url = f"tel:{contact.phone_number}"
    await process_and_send_qr(message, "contact", phone_url, caption)


# Lokatsiya (Location)
@dp.message(F.location)
async def handle_location(message: Message):
    location = message.location
    extra_data = json.dumps({
        "latitude": location.latitude,
        "longitude": location.longitude
    })
    maps_url = f"https://www.google.com/maps?q={location.latitude},{location.longitude}"
    database.save_media("location", extra_data=extra_data, caption=f"{location.latitude}, {location.longitude}")

    # Directly encode Google Maps URL so camera opens map directly in 1 click!
    await process_and_send_qr(message, "location", maps_url, f"Google Maps: {maps_url}")


# Matn yoki Havola (Text or URL)
@dp.message(F.text)
async def handle_text(message: Message):
    user_id = message.from_user.id
    lang = database.get_user_language(user_id)

    if not lang:
        await message.answer(
            locales.TEXTS["uz"]["select_language"],
            reply_markup=get_language_keyboard(),
            parse_mode=ParseMode.HTML
        )
        return

    text = message.text.strip()

    if not text:
        await message.answer(locales.get_text(lang, "enter_valid"))
        return

    if len(text) > 2000:
        await message.answer(locales.get_text(lang, "text_too_long"))
        return

    # Veb-sayt yoki video havolasi tekshiriladi
    direct_url = parse_url(text)
    if direct_url:
        # Skanerlanganda to'g'ridan-to'g'ri videoga yoki saytga kirib ketadigan QR kodi
        await process_and_send_qr(message, "url", direct_url, text)
    else:
        # Oddiy matn bo'lsa
        await process_and_send_qr(message, "text", text, text)


@dp.message()
async def handle_other(message: Message):
    user_id = message.from_user.id
    lang = database.get_user_language(user_id) or "uz"
    await message.answer(locales.get_text(lang, "unknown_media"))


async def main():
    global BOT_USERNAME
    database.init_db()
    bot_info = await bot.get_me()
    BOT_USERNAME = bot_info.username
    logging.info(f"Direct QR Bot starting: @{BOT_USERNAME}")
    print(f"Bot muvaffaqiyatli ishga tushdi! Username: @{BOT_USERNAME}")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
