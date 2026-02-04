import sqlite3
import os
from datetime import datetime

import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("news.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                source TEXT,
                url TEXT,
                category TEXT
            )
        """)
        self.conn.commit()




    def insert_item(self, item):
        cursor = self.conn.cursor()
        cursor.execute(
        "INSERT INTO news (title, source, url, category) VALUES (?, ?, ?, ?)",
        (
            item["title"],
            item["source"],
            item["url"],
            item.get("category", "General")
        )
    )
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
    
    def fetch_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT title, source, url, category FROM news")
        rows = cursor.fetchall()

        return [
        {
            "title": row[0],
            "source": row[1],
            "url": row[2],
            "category": row[3]
        }
        for row in rows
    ]

