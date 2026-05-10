from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data.base import Base
from app.data.session import engine

# import all models so SQLAlchemy knows about them
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
)

# creates all tables on startup if they don't exist
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "SquadPath API is running"}