# Home Library Management System

A simple three-tier web application for managing a personal collection of books.

The application allows users to add, edit, delete, search, filter, and manage the availability of books through a web-based interface. Book data is stored in PostgreSQL.

---

## Architecture

The application follows a three-tier architecture:

```text
                    Browser
                       |
                       v
              +------------------+
              | Presentation     |
              | Flask + Jinja2   |
              | HTML/CSS/JS      |
              +--------+---------+
                       |
                       v
              +------------------+
              | Application      |
              | Flask Routes     |
              | BookService      |
              | Validation       |
              +--------+---------+
                       |
                       v
              +------------------+
              | Data             |
              | BookRepository   |
              | PostgreSQL       |
              +------------------+
````

### Application Flow

```text
User Request
     ↓
Flask Route
     ↓
Book Service
     ↓
Book Repository
     ↓
PostgreSQL
     ↓
Response
     ↓
Web Browser
```

---

## Technologies

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Application development      |
| Flask      | Web framework                |
| Jinja2     | Server-side HTML rendering   |
| PostgreSQL | Relational database          |
| Psycopg    | PostgreSQL database driver   |
| HTML5      | Web page structure           |
| CSS3       | Application styling          |
| JavaScript | Client-side functionality    |
| pip        | Python dependency management |
| venv       | Isolated Python environment  |
| pytest     | Testing                      |

---

## Features

* Add books
* Edit books
* Delete books
* Search books by title or author
* Filter books by genre
* Mark books as available or borrowed
* View total number of books
* View available books
* View borrowed books
* Responsive web interface
* PostgreSQL persistence

---

## Project Structure

```text
home-library-management-system/
│
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── schema.sql
│
├── repositories/
│   ├── __init__.py
│   └── book_repository.py
│
├── services/
│   ├── __init__.py
│   └── book_service.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── book-form.html
│   ├── about.html
│   ├── contact.html
│   └── 404.html
│
└── static/
    ├── style.css
    └── app.js
```

---

## Requirements

Make sure the following are installed:

* Python 3.11+
* PostgreSQL 15+
* pip

Check Python:

```bash
python3 --version
```

Check PostgreSQL:

```bash
psql --version
```

---

# Local Setup

## 1. Clone the Repository

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd home-library-management-system
```

---

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

After activation, your terminal should show:

```text
(.venv)
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Verify installed packages:

```bash
pip list
```

---

# PostgreSQL Setup

## 4. Install PostgreSQL

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

Start PostgreSQL:

```bash
sudo systemctl start postgresql
```

Enable PostgreSQL at boot:

```bash
sudo systemctl enable postgresql
```

Check the service:

```bash
sudo systemctl status postgresql
```

---

## 5. Create Database and User

Open PostgreSQL:

```bash
sudo -u postgres psql
```

Run:

```sql
CREATE DATABASE library_db;

CREATE USER library_user WITH PASSWORD 'library_password';

GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
```

Exit:

```sql
\q
```

---

## 6. Configure Database Connection

Set the `DATABASE_URL` environment variable:

```bash
export DATABASE_URL="postgresql://library_user:library_password@localhost:5432/library_db"
```

Verify:

```bash
echo $DATABASE_URL
```

The application reads this environment variable instead of hard-coding database credentials.

---

# Database Initialization

## 7. Create Tables and Sample Data

Run:

```bash
python -c "from db import init_db; init_db()"
```

This executes:

```text
database/schema.sql
```

and creates the `books` table with sample records.

---

### PostgreSQL Schema Permissions

If you get:

```text
psycopg.errors.InsufficientPrivilege:
permission denied for schema public
````

the PostgreSQL user can access the database but does not have permission to create tables in the `public` schema.

Connect as the PostgreSQL administrator:

```bash
sudo -u postgres psql
```

Then run:

```sql
\c library_db

GRANT USAGE, CREATE ON SCHEMA public TO library_user;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO library_user;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO library_user;
```

Exit PostgreSQL:

```sql
\q
```

Then set the database connection variable:

```bash
export DATABASE_URL="postgresql://library_user:library_password@localhost:5432/library_db"
```

Verify:

```bash
echo $DATABASE_URL
```

Initialize the database:

```bash
python -c "from db import init_db; init_db()"
```

If successful, the required database tables will be created.

# Run the Application

## 8. Start the Server

```bash
python app.py
```

The application listens on:

```text
0.0.0.0:5000
```

Open:

```text
http://localhost:5000
```

For GitHub Codespaces, forward **port 5000** and open the forwarded URL in your browser.

---

# Application Usage

### Dashboard

The home page displays:

* Total books
* Available books
* Borrowed books
* Book collection

### Add a Book

Click:

```text
+ Add Book
```

Enter:

* Book title
* Author
* Genre
* Published year

### Edit a Book

Click:

```text
Edit
```

Modify the book information and save it.

### Borrow / Return

Use:

```text
Borrow
```

or:

```text
Return
```

to change the book availability.

### Delete

Click:

```text
Delete
```

and confirm the operation.

### Search

Search using:

* Book title
* Author

### Filter

Filter books by genre.

---

# Testing

The project includes pytest as the testing dependency.

Run:

```bash
pytest
```

---

# Important Runtime Files

### `app.py`

Main Flask application.

Responsible for:

* Application startup
* Routes
* Request handling
* Template rendering

### `db.py`

Database connection and schema initialization.

### `services/book_service.py`

Contains application/business logic and validation.

### `repositories/book_repository.py`

Handles PostgreSQL queries.

### `database/schema.sql`

Creates the database table and sample records.

### `requirements.txt`

Contains Python dependency versions.

---

# Python Dependency Management

Install dependencies:

```bash
pip install -r requirements.txt
```

View installed packages:

```bash
pip list
```

Generate a dependency snapshot:

```bash
pip freeze
```

The project dependency definition is maintained in:

```text
requirements.txt
```

Do not commit:

```text
.venv/
```

---

# Environment Configuration

The application uses:

```text
DATABASE_URL
```

Example:

```bash
export DATABASE_URL="postgresql://library_user:library_password@localhost:5432/library_db"
```

Do not commit real passwords or secrets to Git.

---

# Useful Verification Commands

Check Python:

```bash
python3 --version
```

Check active Python:

```bash
which python
```

Check installed dependencies:

```bash
pip list
```

Check PostgreSQL:

```bash
sudo systemctl status postgresql
```

Check database:

```bash
sudo -u postgres psql -l
```

Check application port:

```bash
ss -lntp | grep 5000
```

Check application response:

```bash
curl -I http://localhost:5000
```

Check CSS:

```bash
curl -I http://localhost:5000/static/style.css
```

---

# DevOps Practice

This project can be used to practice:

```text
Git
  ↓
Python Environment
  ↓
Dependency Installation
  ↓
Testing
  ↓
PostgreSQL Setup
  ↓
Application Configuration
  ↓
Application Startup
  ↓
Port Verification
  ↓
Browser Access
```

Later deployment practice can include:

```text
Linux Server
    ↓
Python Environment
    ↓
PostgreSQL
    ↓
Environment Variables
    ↓
Application
    ↓
Process Management
    ↓
Reverse Proxy
    ↓
Docker
    ↓
CI/CD
```

---

# Git Workflow

Check changes:

```bash
git status
```

Stage files:

```bash
git add .
```

Commit:

```bash
git commit -m "Add home library management application"
```

Push:

```bash
git push origin main
```

---

# Files That Should NOT Be Committed

The following should remain ignored:

```text
.venv/
__pycache__/
*.pyc
.env
*.db
```

The `.gitignore` file is already configured for these.

---

# Troubleshooting

## `ModuleNotFoundError`

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## `DATABASE_URL environment variable is not set`

Run:

```bash
export DATABASE_URL="postgresql://library_user:library_password@localhost:5432/library_db"
```

---

## PostgreSQL connection refused

Check:

```bash
sudo systemctl status postgresql
```

Start it:

```bash
sudo systemctl start postgresql
```

---

## Password authentication failed

Verify that the PostgreSQL username/password matches the `DATABASE_URL`.

---

## Table does not exist

Initialize the database:

```bash
python -c "from db import init_db; init_db()"
```

---

## Port 5000 is not accessible

Check:

```bash
ss -lntp | grep 5000
```

For Codespaces, make sure port `5000` is forwarded.

---

# License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and sell copies of the Software,
and to permit persons to whom the Software is furnished to do so.
