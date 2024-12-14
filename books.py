from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def say_hello():
    return { "message": "Hello Arun!" }


BOOKS = [
    { "author": "JK Rowling", "book": "Harry Potter", "stock_count": 97 },
    { "author": "Morgan Housel", "book": "Psychology of Money", "stock_count": 25 }
]

@app.get("/books")
async def get_books():
    return { "Books": BOOKS}