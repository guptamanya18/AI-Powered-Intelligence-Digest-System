def create_evaluations_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER,
        keep BOOLEAN,
        relevance_score INTEGER,
        reason TEXT,
        FOREIGN KEY(item_id) REFERENCES items(id)
    )
    """)
