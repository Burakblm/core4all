from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app import models

def get_user_by_email(email, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user

