import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.db_path = os.path.join("data", "digest.db")
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            content TEXT,
            url TEXT UNIQUE,
            published_at TEXT,
            engagement INTEGER
        )
        """)
        self.conn.commit()

    def insert_item(self, item: dict):
        self.cursor.execute("""
        INSERT OR IGNORE INTO items
        (source, title, content, url, published_at, engagement)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item.get("source"),
            item.get("title"),
            item.get("content"),
            item.get("url"),
            item.get("published_at", datetime.utcnow().isoformat()),
            item.get("engagement", 0)
        ))
        self.conn.commit()

    def get_daily_items(self):
        self.cursor.execute("""
        SELECT title, content, url
        FROM items
        ORDER BY id DESC
        LIMIT 10
        """)
        rows = self.cursor.fetchall()
        return [
            {"title": r[0], "content": r[1], "url": r[2]}
            for r in rows
        ]
