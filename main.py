import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import todo_router, index_router
from database.config import Base, engine

app = FastAPI()

# CORS middleware qo'shish
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Barcha domendan kelgan so'rovlarga ruxsat
    allow_credentials=True,
    allow_methods=["*"],  # Barcha metodlarga ruxsat
    allow_headers=["*"],  # Barcha headlarga ruxsat
)

# Routelarni qo'shish
app.include_router(todo_router)
app.include_router(index_router)

# Ma'lumotlar bazasini yaratish
Base.metadata.create_all(bind=engine)

# Uvicorn serverini ishga tushirish
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
