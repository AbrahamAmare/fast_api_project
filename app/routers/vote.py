from fastapi import Depends, Response, status, HTTPException, APIRouter

from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import desc
from .. import oauth2

router = APIRouter(
    prefix='/votes',
    tags=['Votes']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {vote.post_id} does not exist")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    voted = vote_query.first()
    print(vote)
    if (vote.dir == 1):
        if voted:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{current_user.id} have already voted on {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully voted"}
    else:
        if not voted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}
