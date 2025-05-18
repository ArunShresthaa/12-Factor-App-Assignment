import logging
import uvicorn
from fastapi import FastAPI
from settings import settings
from routers.calculator import router as calc_router

app = FastAPI()
app.include_router(calc_router, prefix="/calc")


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    logging.basicConfig(level=settings.log_level.upper())
    uvicorn.run(
        "main:app", host="0.0.0.0", port=settings.port,
        log_level=settings.log_level
    )
