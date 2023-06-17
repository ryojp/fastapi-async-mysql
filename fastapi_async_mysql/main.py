from databases import Database
from fastapi import FastAPI
import uvicorn
import os

PORT = int(os.environ.get("PORT", "8001"))
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_DB = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASS = os.environ.get("MYSQL_PASSWORD")

app = FastAPI()
database = Database(
    f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DB}"
)


@app.on_event("startup")
async def startup():
    await database.connect()
    query = """CREATE TABLE IF NOT EXISTS HighScores (id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query)


@app.get("/post")
async def post():
    query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
    values = [
        {"name": "Daisy", "score": 92},
        {"name": "Neil", "score": 87},
        {"name": "Carol", "score": 43},
    ]
    await database.execute_many(query=query, values=values)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/list")
async def list():
    query = "SELECT * FROM HighScores"
    rows = await database.fetch_all(query=query)
    return rows


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
