from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

book = [
    {
        "id": 1,
        "title": "Dế Mèn Phiêu Lưu Ký",
        "author": "Tô Hoài",
        "price": 45000,
        "pages": 200
    }
]

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    pages: int

class BookResponse(BookCreate):
    id: int

# Bài 1
@app.post("/books", response_model=BookResponse)
def add_book(book_db: BookCreate):
    book_id = 2

    new_book = {
        "id": book_id,
        "title": book_db.title,
        "author": book_db.author,
        "price": book_db.price,
        "pages": book_db.pages
    }

    book.append(new_book)
    book_id += 1

    return new_book

# Bài 2
@app.get("/books/{id}", response_model=BookResponse)
def get_book(id: int):
    for b in book:
        if b["id"] == id:
            return b

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

