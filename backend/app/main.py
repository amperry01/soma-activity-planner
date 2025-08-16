from fastapi import FastAPI
from app.routes import recommendations, oura_loader

app = FastAPI()

app.include_router(recommendations.router)
app.include_router(oura_loader.router)