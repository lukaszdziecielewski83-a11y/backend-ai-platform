from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def get_projects(db: Session):
    return db.query(Project).all()


def create_project(db: Session, project: ProjectCreate):
    new_project = Project(
        name=project.name,
        description=project.description,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project
