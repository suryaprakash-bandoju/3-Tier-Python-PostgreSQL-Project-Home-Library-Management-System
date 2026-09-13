# Home Library Management System

Simple three-tier Python web application for managing a personal book collection.

## Stack

- Python 3
- Flask
- PostgreSQL
- psycopg
- Jinja2
- HTML/CSS/JavaScript

## Architecture

Browser
→ Flask presentation/routes
→ BookService business logic
→ BookRepository data access
→ PostgreSQL

## Features

- Add books
- Edit books
- Delete books
- Search by title or author
- Filter by genre
- Borrow/return books
- Dashboard statistics

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set the database connection:

```bash
export DATABASE_URL="postgresql://library_user:library_password@localhost:5432/library_db"
```

Initialize the database:

```bash
python -c "from db import init_db; init_db()"
```

Run:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```
