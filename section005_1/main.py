### 가장 빠른!
from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint") 
async def first_api() : # 일단 비동기
    return {"message": "Hello kurt!"}

@app.get("/api-endpoint") 
async def first_api() : # 일단 비동기
    return {"message": "Hello kurt!"}

# uvicorn main:app --reload
# 으로 실행 #디버그 하는 법은 알지만 나중에 천천히~