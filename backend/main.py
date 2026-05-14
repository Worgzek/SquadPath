from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data.base import Base
from app.data.session import engine

# thêm models để SQLAlchemy biết
from app.models import user, roadmap, squad, match

app = FastAPI(
    title="SquadPath API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) #khởi tạo cors, m hình dung cors là thằng an ninh để ccho phép frontend giao tiếp với bacckend tại 2 thằng này khác port

Base.metadata.create_all(bind=engine)

@app.get("/") #cái này là cái route test xem API có chạy không
def root():
    return {"status": "SquadPath API is running"}