from fastapi import FastAPI
from logger import logger

app = FastAPI()

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}
