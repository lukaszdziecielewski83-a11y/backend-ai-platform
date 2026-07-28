from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_database
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import create_project, get_projects

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/", response_model=list[ProjectResponse])
def read_projects(db: Session = Depends(get_database)):
    return get_projects(db)


@router.post("/", response_model=ProjectResponse)
def add_project(
    project: ProjectCreate,
    db: Session = Depends(get_database),
):
    return create_project(db, project)
