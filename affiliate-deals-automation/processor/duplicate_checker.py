def is_duplicate(cursor, title):
    cursor.execute("SELECT 1 FROM deals WHERE title=?", (title,))
    return cursor.fetchone() is not None

