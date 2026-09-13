CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(150) NOT NULL,
    genre VARCHAR(80) NOT NULL,
    published_year INTEGER NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO books (title, author, genre, published_year, available)
SELECT 'The Alchemist', 'Paulo Coelho', 'Fiction', 1988, TRUE
WHERE NOT EXISTS (
    SELECT 1 FROM books WHERE title = 'The Alchemist'
);

INSERT INTO books (title, author, genre, published_year, available)
SELECT 'Atomic Habits', 'James Clear', 'Self Help', 2018, FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM books WHERE title = 'Atomic Habits'
);

INSERT INTO books (title, author, genre, published_year, available)
SELECT 'Clean Code', 'Robert C. Martin', 'Technology', 2008, TRUE
WHERE NOT EXISTS (
    SELECT 1 FROM books WHERE title = 'Clean Code'
);
