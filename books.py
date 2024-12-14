from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

@app.get("/")
async def say_hello():
    return { "message": "Hello Arun!" }


BOOKS = [
    { "category": "fiction", "author": "JK Rowling", "book_name": "Harry Potter", "stock_count": 97 },
    { "category": "fiction", "author": "Frank Hebert", "book_name": "Dune", "stock_count": 97},
    { "category": "fiction", "author": "George Orwell", "book_name": "Animal Farm", "stock_count": 25 },
    { "category": "non fiction", "author": "George Orwell", "book_name": "The Road to Wigan Pier", "stock_count": 25 },
    { "category": "non fiction","author": "Morgan Housel", "book_name": "Psychology of Money", "stock_count": 25 },
    { "category": "non fiction","author": "James Clear", "book_name": "Atomic Habits", "stock_count": 25 },
    { "category": "non fiction", "author": "Yuvan Noa Harari", "book_name": "Sapiens", "stock_count": 25}
]

@app.get("/books/")
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


@app.get("/books")
async def get_books_by_category(category: Optional[str] = None):
    if category is None:
        return BOOKS

    books = []
    for book in BOOKS:
        if(book.get("category").lower() == category):
            books.append(book)

    return books



@app.get("/author/{author}/books")
async def get_books_by_author_and_category(author: str, category: Optional[str] = None):

    books = []
    for book in BOOKS:
        if(((category is None) or (book.get("category").lower() == category)) and (book.get("author").lower() == author.lower())):
            books.append(book)

    return books
