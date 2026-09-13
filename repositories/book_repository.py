from psycopg.rows import dict_row
from db import get_connection


class BookRepository:
    def find_all(self, query="", genre=""):
        sql = """
            SELECT id, title, author, genre, published_year, available
            FROM books
            WHERE 1=1
        """
        params = []

        if query:
            sql += " AND (title ILIKE %s OR author ILIKE %s)"
            pattern = f"%{query}%"
            params.extend([pattern, pattern])

        if genre:
            sql += " AND genre = %s"
            params.append(genre)

        sql += " ORDER BY id DESC"

        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()

    def find_by_id(self, book_id):
        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    SELECT id, title, author, genre, published_year, available
                    FROM books
                    WHERE id = %s
                    """,
                    (book_id,)
                )
                return cursor.fetchone()

    def find_genres(self):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT DISTINCT genre FROM books ORDER BY genre"
                )
                return [row[0] for row in cursor.fetchall()]

    def create(self, book):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO books
                    (title, author, genre, published_year, available)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        book["title"],
                        book["author"],
                        book["genre"],
                        book["published_year"],
                        book["available"]
                    )
                )
            connection.commit()

    def update(self, book_id, book):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE books
                    SET title=%s,
                        author=%s,
                        genre=%s,
                        published_year=%s,
                        available=%s
                    WHERE id=%s
                    """,
                    (
                        book["title"],
                        book["author"],
                        book["genre"],
                        book["published_year"],
                        book["available"],
                        book_id
                    )
                )
                updated = cursor.rowcount > 0
            connection.commit()
            return updated

    def delete(self, book_id):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM books WHERE id=%s",
                    (book_id,)
                )
                deleted = cursor.rowcount > 0
            connection.commit()
            return deleted

    def toggle(self, book_id):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE books SET available = NOT available WHERE id=%s",
                    (book_id,)
                )
                updated = cursor.rowcount > 0
            connection.commit()
            return updated

    def stats(self):
        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    SELECT
                        COUNT(*) AS total,
                        COUNT(*) FILTER (WHERE available) AS available,
                        COUNT(*) FILTER (WHERE NOT available) AS borrowed
                    FROM books
                    """
                )
                return cursor.fetchone()
