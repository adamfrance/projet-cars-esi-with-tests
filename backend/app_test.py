from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import mongomock
from routers.cars import router as cars_router

# CORS middleware
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

# App instantiation with mock database
app = FastAPI(middleware=middleware)
app.include_router(cars_router, prefix="/cars", tags=["cars"])

# Use mock MongoDB client
app.mongodb_client = mongomock.MongoClient()
app.mongodb = app.mongodb_client.db

@app.get("/")
async def root():
    return {"message": "API is running in test mode"}