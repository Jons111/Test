from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine, get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user

Base.metadata.create_all(bind=engine)

from functions.posts import one_post, all_posts, update_post, create_post, post_delete
from schemas.posts import PostCreate, PostUpdate
from schemas.users import UserCurrent

router_post = APIRouter()


@router_post.post('/add', )
def add_post(form: PostCreate, db: Session = Depends(get_db),
             current_post: UserCurrent = Depends(get_current_active_user)):  #
    if create_post(form, current_post, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_post.get('/', status_code=200)
def get_posts(search: str = None, status: bool = True, id: int = 0, page: int = 1, limit: int = 25, db: Session = Depends(get_db),
              current_post: UserCurrent = Depends(
                  get_current_active_user)):  # current_post: Post = Depends(get_current_active_post)
    if id:
        return one_post(id, db)
    else:
        return all_posts(search,status, page, limit, db)


@router_post.put("/update")
def post_update(form: PostUpdate, db: Session = Depends(get_db),
                current_post: UserCurrent = Depends(get_current_active_user)):
    if update_post(form, current_post, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_post.delete('/{id}', status_code=200)
def delete_post(id: int = 0, db: Session = Depends(get_db), current_post: UserCurrent = Depends(
    get_current_active_user)):  # current_post: Post = Depends(get_current_active_post)
    if id:
        return post_delete(id, db)
