# QR-kod Generator Bot

Telegram bot: foydalanuvchi matn yoki link yuboradi, bot QR-kod rasm qilib qaytaradi.

## 1. Bot token olish

1. Telegram'da **@BotFather** ga yozing
2. `/newbot` buyrug'ini yuboring
3. Bot uchun ism va username bering (username `bot` bilan tugashi kerak, masalan `mening_qr_bot`)
4. BotFather sizga token beradi, masalan: `7123456789:AAH...`
5. Shu tokenni `config.py` faylidagi `BOT_TOKEN` ga qo'ying

## 2. Kompyuteringizda ishga tushirish

```bash
# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# Botni ishga tushirish
python3 bot.py
```

Terminalda "Bot ishga tushdi..." deb chiqsa — tayyor. Endi Telegram'da botingizga `/start` yozib sinab ko'ring.

## 3. Bepul hostingga joylash (24/7 ishlashi uchun)

Kompyuteringiz o'chirilganda ham bot ishlashi uchun uni serverga qo'yish kerak. Eng oson bepul variantlar:

### Railway.app (tavsiya etiladi)
1. [railway.app](https://railway.app) da ro'yxatdan o'ting (GitHub bilan)
2. Loyihani GitHub'ga yuklang (repo yarating, fayllarni push qiling)
3. Railway'da "New Project" → "Deploy from GitHub repo"
4. Environment Variables bo'limida `BOT_TOKEN` ni qo'shing (yoki config.py ichida qoldirsangiz ham bo'ladi)
5. Avtomatik deploy bo'ladi

### Render.com
1. [render.com](https://render.com) da "New Background Worker" yarating
2. GitHub repo'ni ulang
3. Build command: `pip install -r requirements.txt`
4. Start command: `python3 bot.py`

**Eslatma:** Token kabi maxfiy ma'lumotlarni GitHub'ga ochiq push qilmang. Buning o'rniga `.env` fayl yoki hosting platformasining "Environment Variables" bo'limidan foydalaning.

## 4. Botni kengaytirish g'oyalari

- QR-kod rangini o'zgartirish imkoniyati (foydalanuvchi rang tanlaydi)
- Logotip bilan QR-kod yasash
- WiFi parolidan QR-kod yasash (maxsus format)
- Statistika: nechta QR-kod yaratilgani
- Inline mode: boshqa chatlarda `@sizning_bot matn` deb yozib QR yasash

## Fayllar tuzilishi

```
qr_bot/
├── bot.py            # Asosiy bot kodi
├── config.py         # Bot tokeni
├── requirements.txt  # Kerakli kutubxonalar
└── README.md         # Shu qo'llanma
```
