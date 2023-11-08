from fastapi import Depends, status, HTTPException, APIRouter

from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from app import utils

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get("/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)

def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="user with the given info does not exist")
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash password
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
