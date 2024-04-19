import uvicorn
from fastapi import FastAPI, APIRouter

from students.router import students_router

app = FastAPI(title="MongoDB+FastAPI")

main_router = APIRouter(prefix="/api/v1")

main_router.include_router(students_router)


@main_router.get("/")
async def get_home_page():
    return "Welcome to MongoDB+FastAPI site"

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(port=10000, app="main:app", reload=True)