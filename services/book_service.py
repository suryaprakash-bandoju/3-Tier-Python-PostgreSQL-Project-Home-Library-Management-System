from repositories.book_repository import BookRepository


class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def list_books(self, query="", genre=""):
        return self.repository.find_all(query, genre)

    def list_genres(self):
        return self.repository.find_genres()

    def get_book(self, book_id):
        return self.repository.find_by_id(book_id)

    def get_stats(self):
        return self.repository.stats()

    def create_book(self, data):
        book = self._validate(data)
        book["available"] = True
        self.repository.create(book)

    def update_book(self, book_id, data):
        book = self._validate(data)
        book["available"] = data.get("available") == "on"
        return self.repository.update(book_id, book)

    def delete_book(self, book_id):
        return self.repository.delete(book_id)

    def toggle_availability(self, book_id):
        return self.repository.toggle(book_id)

    @staticmethod
    def _validate(data):
        title = data.get("title", "").strip()
        author = data.get("author", "").strip()
        genre = data.get("genre", "").strip()
        year_text = data.get("published_year", "").strip()

        if not title:
            raise ValueError("Title is required.")
        if not author:
            raise ValueError("Author is required.")
        if not genre:
            raise ValueError("Genre is required.")

        try:
            year = int(year_text)
        except ValueError as exc:
            raise ValueError("Published year must be a number.") from exc

        return {
            "title": title,
            "author": author,
            "genre": genre,
            "published_year": year
        }
