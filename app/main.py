from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Backend AI Platform",
    description="Production-oriented backend platform",
    version="1.0.0"
)


app.include_router(router)
