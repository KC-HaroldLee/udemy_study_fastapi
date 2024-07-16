from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': '제목하나', 'author' : '테리이글턴', 'category' : 'literature'},
    {'title': '제목둘', 'author' : '바흐찐', 'category' : 'literature'},
    {'title': '제목셋', 'author' : '소쉬르', 'category' : 'linguistics'},
    {'title': '제목넷', 'author' : '촘스키', 'category' : 'linguistics'},
    {'title': '제목다섯', 'author' : '프로이트', 'category' : 'psychoanalysis'},
    {'title': '제목여섯', 'author' : '라캉', 'category' : 'psychoanalysis'},
]

# 없는 것은 {"detail":"Not Found"} 을 반환한다.
@app.get("/")
async def index():
    return {"message" : " HELLO!"}

@app.get("/books")
async def read_all_books():
    return BOOKS

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param:str): # 여기서 타입을 강제할 수 있다.
#     return {'dynamic_param' : dynamic_param}

@app.get("/books/{dynamic_param}")
async def read_book(book_title:str): # 여기서 타입을 강제할 수 있다.
    for book in BOOKS :
        if book['title'].casefold() == book_title.casefold() :
            return book

# 여러가지 실행법
# fastapi run ./main.py
# fastapi dev ./main.py
# uvicorn main:app --reload
