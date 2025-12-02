from fastapi import FastAPI
from app.api import router

app = FastAPI(title="FileIntake AI Microservice")
app.include_router(router)