from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.core.db import get_db
from app import models, crud

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    first_user = crud.get_user_by_email(user.email, db=db)
    if first_user:
        raise HTTPException(
            status_code=400,
            detail="this email is already in use"
        )

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


