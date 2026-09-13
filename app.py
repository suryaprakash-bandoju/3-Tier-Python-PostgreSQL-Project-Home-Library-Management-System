from flask import Flask, render_template, request, redirect, url_for, flash
from db import init_db
from services.book_service import BookService

app = Flask(__name__)
app.secret_key = "dev-secret-key"

service = BookService()


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    genre = request.args.get("genre", "").strip()

    books = service.list_books(query=query, genre=genre)
    genres = service.list_genres()
    stats = service.get_stats()

    return render_template(
        "index.html",
        books=books,
        genres=genres,
        selected_genre=genre,
        query=query,
        stats=stats
    )


@app.route("/books/new")
def new_book():
    return render_template("book-form.html", book=None, form_title="Add Book")


@app.route("/books", methods=["POST"])
def create_book():
    try:
        service.create_book(request.form.to_dict())
        flash("Book added successfully.", "success")
        return redirect(url_for("index"))
    except ValueError as exc:
        flash(str(exc), "error")
        return render_template(
            "book-form.html",
            book=request.form.to_dict(),
            form_title="Add Book"
        ), 400


@app.route("/books/<int:book_id>/edit")
def edit_book(book_id):
    book = service.get_book(book_id)
    if not book:
        return render_template("404.html"), 404
    return render_template("book-form.html", book=book, form_title="Edit Book")


@app.route("/books/<int:book_id>/edit", methods=["POST"])
def update_book(book_id):
    try:
        service.update_book(book_id, request.form.to_dict())
        flash("Book updated successfully.", "success")
        return redirect(url_for("index"))
    except ValueError as exc:
        book = request.form.to_dict()
        book["id"] = book_id
        flash(str(exc), "error")
        return render_template(
            "book-form.html",
            book=book,
            form_title="Edit Book"
        ), 400


@app.route("/books/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    if service.delete_book(book_id):
        flash("Book deleted successfully.", "success")
    else:
        flash("Book not found.", "error")
    return redirect(url_for("index"))


@app.route("/books/<int:book_id>/toggle", methods=["POST"])
def toggle_availability(book_id):
    service.toggle_availability(book_id)
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
