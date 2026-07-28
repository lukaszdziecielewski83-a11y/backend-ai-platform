from fastapi import APIRouter

from app.api.projects import router as projects_router

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Backend AI Platform is running"
    }


router.include_router(projects_router)
