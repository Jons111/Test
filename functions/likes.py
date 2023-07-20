from passlib.context import CryptContext
from sqlalchemy.orm import joinedload

from fastapi import HTTPException

from functions.posts import one_post
from models.likes import Likes
from models.posts import Posts

from utils.pagination import pagination


def all_likes(status, page, limit, db):
    if status in [True, False]:
        status_filter = Likes.status == status
    else:
        status_filter = Likes.id > 0

    likes = db.query(Likes).filter(status_filter, ).order_by(Likes.name.asc())
    if page and limit:
        return pagination(likes, page, limit)
    else:
        return likes.all()


def one_like(id, db):
    return db.query(Likes).filter(Likes.id == id).first()


def create_like(form, user, db):
    post = db.query(Posts).filter(Posts.id == form.post_id).first()
    if post.user_id == user.id:
        raise HTTPException(status_code=400, detail="you can not like to your posts !!!")
    if one_post(form.post_id,db) is None:
        raise HTTPException(status_code=400, detail="Post does not exist !!!")
    new_like_db = Likes(
        like=form.like,
        user_id=user.id,
        post_id=form.post_id, )

    db.add(new_like_db)
    db.commit()
    db.refresh(new_like_db)
    if form.like:
        like_number = post.likes + 1
        db.query(Posts).filter(Posts.id == form.post_id).update({
            Posts.likes: like_number, })
        db.commit()
    else:
        dislike_number = post.dislikes + 1
        db.query(Posts).filter(Posts.id == form.post_id).update({
                Posts.dislikes: dislike_number,})
        db.commit()

    return new_like_db


def update_like(form, user, db):
    if one_like(form.id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli foydalanuvchi mavjud emas")

    db.query(Likes).filter(Likes.id == form.id).update({
        Likes.like: form.title,
        Likes.post_id: form.post_id,
        Likes.status: form.status,
        Likes.user_id: user.id,

    })
    db.commit()

    return one_like(form.id, db)


def like_delete(id, db):
    if one_like(id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli ma'lumot mavjud emas")
    db.query(Likes).filter(Likes.id == id).update({
        Likes.status: False,
    })
    db.commit()
    return {"date": "Ma'lumot o'chirildi !"}
