from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine, get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user

Base.metadata.create_all(bind=engine)

from functions.likes import one_like, all_likes, update_like, create_like, like_delete
from schemas.likes import LikeCreate, LikeUpdate
from schemas.users import UserCurrent

router_like = APIRouter()


@router_like.post('/add', )
def add_like(form: LikeCreate, db: Session = Depends(get_db),
             current_like: UserCurrent = Depends(get_current_active_user)):  #
    if create_like(form, current_like, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_like.get('/', status_code=200)
def get_likes(status: bool = True, id: int = 0, page: int = 1, limit: int = 25, db: Session = Depends(get_db),
              current_like: UserCurrent = Depends(
                  get_current_active_user)):  # current_like: Like = Depends(get_current_active_like)
    if id:
        return one_like(id, db)
    else:
        return all_likes(status, page, limit, db)


@router_like.put("/update")
def like_update(form: LikeUpdate, db: Session = Depends(get_db),
                current_like: UserCurrent = Depends(get_current_active_user)):
    if update_like(form, current_like, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_like.delete('/{id}', status_code=200)
def delete_like(id: int = 0, db: Session = Depends(get_db), current_like: UserCurrent = Depends(
    get_current_active_user)):  # current_like: Like = Depends(get_current_active_like)
    if id:
        return like_delete(id, db)
