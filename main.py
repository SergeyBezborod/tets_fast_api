from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("dropped")
    await create_tables()
    print("created")
    yield
    print("off")


application = FastAPI(lifespan=lifespan)
application.include_router(task_router)


@application.get("/")
async def root():
    return {"message": "FastAPI is working!"}
