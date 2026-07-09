from fastapi import FastAPI

from app.routers import math

app = FastAPI()
app.include_router(math.router)
