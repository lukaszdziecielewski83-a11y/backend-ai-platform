from fastapi import FastAPI

app = FastAPI(
    title="Backend AI Platform",
    description="Production-oriented backend platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Backend AI Platform is running"
    }
