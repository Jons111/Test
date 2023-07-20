from passlib.context import CryptContext
from sqlalchemy.orm import joinedload

pwd_context = CryptContext(schemes=['bcrypt'])

from fastapi import HTTPException
from models.posts import Posts

from utils.pagination import pagination


def all_posts(search, status, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Posts.title.like(search_formatted) | Posts.content.like(search_formatted)
    else:
        search_filter = Posts.id > 0
    if status in [True, False]:
        status_filter = Posts.status == status
    else:
        status_filter = Posts.id > 0

    posts = db.query(Posts).options(joinedload(Posts.author),joinedload(Posts.like)).filter(search_filter, status_filter, ).order_by(Posts.id.desc())
    if page and limit:
        return pagination(posts, page, limit)
    else:
        return posts.all()


def one_post(id, db):
    return db.query(Posts).options(joinedload(Posts.author),joinedload(Posts.like)).filter(Posts.id == id).first()


def create_post(form, user, db):
    new_post_db = Posts(
        title=form.title,
        content=form.content,
        user_id=user.id

    )
    db.add(new_post_db)
    db.commit()
    db.refresh(new_post_db)

    return new_post_db


def update_post(form, user, db):
    if one_post(form.id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli foydalanuvchi mavjud emas")
    post_verification = db.query(Posts).filter(Posts.postname == form.postname).first()
    if post_verification and post_verification.id != form.id:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud")

    db.query(Posts).filter(Posts.id == form.id).update({
        Posts.title: form.title,
        Posts.content: form.content,
        Posts.status: form.status,
        Posts.user_id: user.id,

    })
    db.commit()

    return one_post(form.id, db)


def post_delete(id, db):
    if one_post(id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli ma'lumot mavjud emas")
    db.query(Posts).filter(Posts.id == id).update({
        Posts.status: False,
    })
    db.commit()
    return {"date": "Ma'lumot o'chirildi !"}
