from typing import Optional # 까먹고 있었음
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field # dataclass보다 훨씬 나음
from starlette import status # 통신종류같은데
from lib.book import Book, BOOKS

class BookRequest(BaseModel):
    # 스웨거에 연동됨
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1900, lt=2031)



app = FastAPI()

# 이건 언제나 만들려고한다.
@app.get("/")
async def index():
    return {"message" : "this is index!!!"}

# 전체 조회
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

# id 조회 : 현재 1~6까지 있음
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)): # int = Path(gt=0)로 인해 
                                                # 다음과 같은 에러가 나뉘어서 나온다. Error: Unprocessable Entity/Error: Not Found
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

# 이것도 결국 
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)): # Query Req이므로 
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)): # 그치 ? Query
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

#################### 드디어

# 단순히 마지막 번호의 숫자+1
def _find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(_find_book_id(new_book))

#### put, delete 생략