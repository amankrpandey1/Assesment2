from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.insta import service, schemas

router = APIRouter()



@router.post("/post/", response_model=schemas.PostCreate)
def create_post(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db=db, item=item)


@router.get("/post/", response_model=List[schemas.PostList])
def get_post_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_posts(db=db, skip=skip, limit=limit)


@router.get("/post/{post_id}", response_model=schemas.PostSingle)
def get_post_detail(post_id: int, db: Session = Depends(get_db)):
    return service.get_post_single(db=db, post_id=post_id)
