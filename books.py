from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def say_hello():
    return { "message": "Hello Arun!" }


BOOKS = [
    { "author": "JK Rowling", "book_name": "Harry Potter", "stock_count": 97 },
    { "author": "Morgan Housel", "book_name": "Psychology of Money", "stock_count": 25 }
]

@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/my_book")
async def get_books():
    return { "book": "MY BOOK." }

@app.get("/books/{book_name}")
async def get_book(book_name: str):
    for book in BOOKS:
        if(book.get("book_name").lower() == book_name.lower()):
            return book

    return { "error": "book not found", "book": book_name}
