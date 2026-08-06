from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

sach_mau = [
    {
        "id": 1,
        "ten_sach": "Nhà Giả Kim",
        "tac_gia": "Paulo Coelho",
        "nam_xuat_ban": 1988,
        "so_luong": 5
    }
]

app = FastAPI()

class Book(BaseModel):
    id: int
    ten_sach: str
    tac_gia: str
    nam_xuat_ban: int
    so_luong: int

@app.post("/api/v1/books", response_model=Book)
def add_book(book: Book):
    sach_mau.append(book.model_dump())
    return book

@app.get("/api/v1/books", response_model=list[Book])
def get_all_books():
    return sach_mau

@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in sach_mau:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

@app.put("/api/v1/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: Book):
    for index, book in enumerate(sach_mau):
        if book["id"] == book_id:
            sach_mau[index] = book_update.model_dump()
            return sach_mau[index]

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

@app.delete("/api/v1/books")
def delete_book(book_id: int):
    for index, book in enumerate(sach_mau):
        if book["id"] == book_id:
            deleted_book = sach_mau.pop(index)
            return {
                "message": "Xóa sách thành công",
                "book": deleted_book
            }

    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )