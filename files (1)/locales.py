# locales.py

TEXTS = {
    "uz": {
        "select_language": "🌐 <b>Iltimos, tilni tanlang:</b>\nПожалуйста, выберите язык:\nPlease select a language:",
        "lang_changed": "✅ Til muvaffaqiyatli tanlandi: 🇺🇿 <b>O'zbekcha</b>",
        "welcome": (
            "👋 Salom! Men <b>Universal QR-kod generatori</b> botiman.\n\n"
            "Menga <b>ISTALGAN NARSANI</b> yuboring — men uni darhol QR-kodga aylantirib beraman! 🚀\n\n"
            "<b>📱 QR-kod qilishingiz mumkin bo'lgan narsalar:</b>\n"
            "• 🖼 <b>Rasm</b> va foto fayllar\n"
            "• 🎥 <b>Video</b> va video roliklar\n"
            "• 📁 <b>Fayllar va Hujjatlar</b> (PDF, Word, ZIP, APK va h.k.)\n"
            "• 🎨 <b>Stikerlar</b>\n"
            "• 🎵 <b>Musiqa va Ovozli xabarlar</b>\n"
            "• ⭕ <b>Video xabarlar (Krug)</b>\n"
            "• 🌐 <b>Veb-sayt havolalari</b> (https://...)\n"
            "• 📝 <b>Matnlar</b> va ma'lumotlar\n"
            "• 👤 <b>Kontaktlar</b> va 📍 <b>Lokatsiyalar</b>\n\n"
            "<b>✨ Qanday ishlaydi?</b>\n"
            "Istalgan narsani yuborasiz — bot sizga QR-kod beradi. "
            "Ushbu QR-kodni istalgan telefon kamerasi bilan skanerlagan odam "
            "siz yuborgan narsani ko'ra oladi!\n\n"
            "Sinab ko'ring! 👇 Yuboring:"
        ),
        "help": (
            "ℹ️ <b>Qanday ishlatiladi?</b>\n\n"
            "1. Botga rasm, video, fayl, stiker, audio, kontakt, geolokatsiya yoki matn yuboring.\n"
            "2. Bot sizga shu narsa uchun maxsus QR-kod rasmini va havolasini tayyorlab beradi.\n"
            "3. QR-kodni chop etishingiz, saqlashingiz yoki do'stlaringizga yuborishingiz mumkin.\n"
            "4. QR-kod skanerlanganda ushbu fayl/rasm/video avtomatik ravishda ochiladi.\n\n"
            "🌐 Tilni o'zgartirish uchun /lang buyrug'ini bosing."
        ),
        "qr_processing": "⏳ QR-kod tayyorlanmoqda...",
        "qr_ready": "✅ <b>{title} uchun QR-kod tayyor!</b>",
        "qr_link": "🔗 <b>Havola:</b> <code>{link}</code>",
        "qr_scan_info": "📱 <i>Ushbu QR-kodni istalgan telefon kamerasi bilan skanerlasangiz, yuborilgan {title} ochiladi!</i>",
        "error_gen": "❌ QR-kod yaratishda xatolik yuz berdi. Qayta urinib ko'ring.",
        "media_not_found": "⚠️ Kechirasiz, ushbu QR-kodga biriktirilgan fayl yoki ma'lumot topilmadi.",
        "text_too_long": "⚠️ Matn juda uzun. Iltimos, 2000 belgidan qisqaroq matn yuboring.",
        "enter_valid": "⚠️ Iltimos, matn, fayl yoki link yuboring.",
        "unknown_media": "⚠️ Yuborilgan obyekt turini tanib bo'lmadi.",
        "btn_change_lang": "🌐 Tilni o'zgartirish",
        "types": {
            "photo": "Rasm",
            "video": "Video",
            "document": "Fayl / Hujjat",
            "sticker": "Stiker",
            "audio": "Audio",
            "voice": "Ovozli xabar",
            "video_note": "Video xabar",
            "animation": "GIF / Animatsiya",
            "contact": "Kontakt",
            "location": "Lokatsiya",
            "url": "Havola (URL)",
            "text": "Matn"
        }
    },
    "ru": {
        "select_language": "🌐 <b>Пожалуйста, выберите язык:</b>\nIltimos, tilni tanlang:\nPlease select a language:",
        "lang_changed": "✅ Язык успешно выбран: 🇷🇺 <b>Русский</b>",
        "welcome": (
            "👋 Привет! Я бот <b>Генератор Universal QR-кодов</b>.\n\n"
            "Отправьте мне <b>ЧТО УГОДНО</b> — и я мгновенно превращу это в QR-код! 🚀\n\n"
            "<b>📱 Что вы можете превратить в QR-код:</b>\n"
            "• 🖼 <b>Фотографии</b> и изображения\n"
            "• 🎥 <b>Видео</b> и ролики\n"
            "• 📁 <b>Файлы и Документы</b> (PDF, Word, ZIP, APK и т.д.)\n"
            "• 🎨 <b>Стикеры</b>\n"
            "• 🎵 <b>Музыку и Голосовые сообщения</b>\n"
            "• ⭕ <b>Видеосообщения (Кружочки)</b>\n"
            "• 🌐 <b>Ссылки на сайты</b> (https://...)\n"
            "• 📝 <b>Тексты</b> и данные\n"
            "• 👤 <b>Контакты</b> и 📍 <b>Локации</b>\n\n"
            "<b>✨ Как это работает?</b>\n"
            "Вы отправляете любой файл или текст — бот выдает вам QR-код. "
            "Каждый, кто отсканирует этот QR-код камерой любого телефона, "
            "сможет открыть ваш файл или видео!\n\n"
            "Попробуйте прямо сейчас! 👇 Отправьте что-нибудь:"
        ),
        "help": (
            "ℹ️ <b>Как использовать:</b>\n\n"
            "1. Отправьте боту фото, видео, файл, стикер, аудио, контакт, геопозицию или текст.\n"
            "2. Бот создаст для вас QR-код и готовую ссылку.\n"
            "3. Вы можете распечатать QR-код или переслать друзьям.\n"
            "4. При сканировании QR-кода файл/видео откроется автоматически.\n\n"
            "🌐 Нажмите /lang для смены языка."
        ),
        "qr_processing": "⏳ Генерируется QR-код...",
        "qr_ready": "✅ <b>QR-код для {title} готов!</b>",
        "qr_link": "🔗 <b>Ссылка:</b> <code>{link}</code>",
        "qr_scan_info": "📱 <i>При сканировании этого QR-кода откроется ваш(а) {title}!</i>",
        "error_gen": "❌ Произошла ошибка при создании QR-кода. Попробуйте еще раз.",
        "media_not_found": "⚠️ Извините, файл или данные, привязанные к этому QR-коду, не найдены.",
        "text_too_long": "⚠️ Текст слишком длинный. Пожалуйста, отправьте текст короче 2000 символов.",
        "enter_valid": "⚠️ Пожалуйста, отправьте текст, файл или ссылку.",
        "unknown_media": "⚠️ Не удалось распознать тип объекта.",
        "btn_change_lang": "🌐 Сменить язык",
        "types": {
            "photo": "Фотография",
            "video": "Видео",
            "document": "Файл / Документ",
            "sticker": "Стикер",
            "audio": "Аудио",
            "voice": "Голосовое сообщение",
            "video_note": "Видеосообщение",
            "animation": "GIF / Анимация",
            "contact": "Контакт",
            "location": "Локация",
            "url": "Ссылка (URL)",
            "text": "Текст"
        }
    },
    "en": {
        "select_language": "🌐 <b>Please select a language:</b>\nIltimos, tilni tanlang:\nПожалуйста, выберите язык:",
        "lang_changed": "✅ Language successfully set to: 🇬🇧 <b>English</b>",
        "welcome": (
            "👋 Hello! I am the <b>Universal QR Code Generator</b> bot.\n\n"
            "Send me <b>ANYTHING</b> — and I will instantly turn it into a QR code! 🚀\n\n"
            "<b>📱 What you can turn into a QR code:</b>\n"
            "• 🖼 <b>Photos</b> and images\n"
            "• 🎥 <b>Videos</b> and clips\n"
            "• 📁 <b>Files & Documents</b> (PDF, Word, ZIP, APK, etc.)\n"
            "• 🎨 <b>Stickers</b>\n"
            "• 🎵 <b>Music & Voice messages</b>\n"
            "• ⭕ <b>Video notes</b>\n"
            "• 🌐 <b>Website Links</b> (https://...)\n"
            "• 📝 <b>Text</b> and notes\n"
            "• 👤 <b>Contacts</b> & 📍 <b>Locations</b>\n\n"
            "<b>✨ How does it work?</b>\n"
            "Send any file, photo, or text — the bot gives you a QR code. "
            "Anyone scanning this QR code with their smartphone camera "
            "will be able to view your content!\n\n"
            "Try it out! 👇 Send something:"
        ),
        "help": (
            "ℹ️ <b>How to use:</b>\n\n"
            "1. Send a photo, video, file, sticker, audio, contact, location, or text to the bot.\n"
            "2. The bot generates a QR code image and a deep link for you.\n"
            "3. Print or share the QR code with anyone.\n"
            "4. Scanning the QR code automatically opens the file/media.\n\n"
            "🌐 Type /lang to change language."
        ),
        "qr_processing": "⏳ Generating QR code...",
        "qr_ready": "✅ <b>QR Code ready for {title}!</b>",
        "qr_link": "🔗 <b>Link:</b> <code>{link}</code>",
        "qr_scan_info": "📱 <i>Scan this QR code with any phone camera to view the {title}!</i>",
        "error_gen": "❌ Error creating QR code. Please try again.",
        "media_not_found": "⚠️ Sorry, the file or data linked to this QR code was not found.",
        "text_too_long": "⚠️ Text is too long. Please send text under 2000 characters.",
        "enter_valid": "⚠️ Please send text, a file, or a link.",
        "unknown_media": "⚠️ Unrecognized media type.",
        "btn_change_lang": "🌐 Change language",
        "types": {
            "photo": "Photo",
            "video": "Video",
            "document": "File / Document",
            "sticker": "Sticker",
            "audio": "Audio",
            "voice": "Voice message",
            "video_note": "Video note",
            "animation": "GIF / Animation",
            "contact": "Contact",
            "location": "Location",
            "url": "Link (URL)",
            "text": "Text"
        }
    }
}


def get_text(lang: str, key: str, **kwargs) -> str:
    """Til va kalit bo'yicha matnni oladi."""
    if lang not in TEXTS:
        lang = "uz"
    
    text = TEXTS.get(lang, {}).get(key, TEXTS["uz"].get(key, ""))
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


def get_type_title(lang: str, media_type: str) -> str:
    """Media turi nomini kerakli tilda oladi."""
    if lang not in TEXTS:
        lang = "uz"
    types = TEXTS[lang].get("types", {})
    return types.get(media_type, media_type.capitalize())
