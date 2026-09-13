import os
import psycopg


def get_connection():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL environment variable is not set.")
    return psycopg.connect(url)


def init_db():
    schema_path = os.path.join(
        os.path.dirname(__file__), "database", "schema.sql"
    )

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(schema)
        connection.commit()
