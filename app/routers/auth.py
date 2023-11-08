from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils
from .. import oauth2
router = APIRouter(tags=['Auth'])

@router.post('/sign-in', response_model=schemas.Token)
def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You have entered invalid credentials")
    if not utils.verify_password_hash(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You have entered invalid credentials")

    # create jwt token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}
