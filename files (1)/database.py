# database.py
import sqlite3
import uuid
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "qr_media.db")


def init_db():
    """Baza tuzilmasini yaratadi (agar mavjud bo'lmasa)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS media_items (
            id TEXT PRIMARY KEY,
            media_type TEXT NOT NULL,
            file_id TEXT,
            caption TEXT,
            extra_data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_languages (
            user_id INTEGER PRIMARY KEY,
            language_code TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_media(media_type: str, file_id: str = None, caption: str = None, extra_data: str = None) -> str:
    """Yangi media obyektini bazaga saqlaydi va uning unikal ID sini qaytaradi."""
    item_id = uuid.uuid4().hex[:10]
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO media_items (id, media_type, file_id, caption, extra_data)
        VALUES (?, ?, ?, ?, ?)
    """, (item_id, media_type, file_id, caption, extra_data))
    conn.commit()
    conn.close()
    return item_id


def get_media(item_id: str):
    """ID bo'yicha media obyektini oladi."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT media_type, file_id, caption, extra_data FROM media_items WHERE id = ?
    """, (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "media_type": row[0],
            "file_id": row[1],
            "caption": row[2],
            "extra_data": row[3]
        }
    return None


def set_user_language(user_id: int, lang_code: str):
    """Foydalanuvchi tilini bazada saqlaydi yoki yangilaydi."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_languages (user_id, language_code)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET language_code = excluded.language_code
    """, (user_id, lang_code))
    conn.commit()
    conn.close()


def get_user_language(user_id: int) -> str:
    """Foydalanuvchi tilini oladi. Agar belgilanmagan bo'lsa, None qaytaradi."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT language_code FROM user_languages WHERE user_id = ?
    """, (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None
