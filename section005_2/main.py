from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


BOOKS = [
    {"title": "제목하나", "author" : "테리이글턴", "category" : "literature"},
    {"title": "제목둘", "author" : "테리이글턴", "category" : "literature"},
    {"title": "제목셋", "author" : "소쉬르", "category" : "linguistics"},
    {"title": "제목넷", "author" : "촘스키", "category" : "linguistics"},
    {"title": "제목다섯", "author" : "프로이트", "category" : "psychoanalysis"},
    {"title": "제목여섯", "author" : "라캉", "category" : "psychoanalysis"},
]

# 없는 것은 {"detail":"Not Found"} 을 반환한다.
@app.get("/")
async def index():
    return {"message" : " HELLO!"}

# 당연히 스웨거 사용가능 /docs

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title:str): # 여기서 타입을 강제할 수 있다.
    for book in BOOKS :
        if book['title'].casefold() == book_title.casefold() :
            return book
        
@app.get("/books/") # 자 여기서는 주소가 같지만
async def read_category_by_query(category: str): # 함수이름이 다르므로 함수 재정의는 아니다.
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold(): # 처음보는 casefold
            books_to_return.append(book)
    return books_to_return

# 1. path파라미터
# 'http://127.0.0.1:8000/books/byauthor/?author=%EC%86%8C%EC%89%AC%EB%A5%B4'
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

# 2. 1에 +query파라미터 추가
# http://127.0.0.1:8000/books/%EC%86%8C%EC%89%AC%EB%A5%B4/?category=linguistics
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# 직접 입력해야한다는게 좀 불편한디
#  {"title": "제목일곱", "author" : "정호승", "category" : "poet"}
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# put은 거의 안쓰는 걸로 알지만된다는 것을 확인
# ㅋㅋㅋ 근데 스웨거에 색이 입혀져서 보기는 좋네
@app.put("/books/update_book")
async def update_book(updated_book=Body()): # 형 강제가 아님
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# delete도..
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str): # 이게 형강제임
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


# 여러가지 실행법
# fastapi run ./main.py
# fastapi dev ./main.py
# uvicorn main:app --reload
