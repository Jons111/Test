from fastapi import FastAPI

from routes import auth, users,likes,posts

from db import Base, engine

Base.metadata.create_all(bind=engine)

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Test",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}


app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'],

)

app.include_router(
    users.router_user,
    prefix='/user',
    tags=['User section'],

)

app.include_router(
    posts.router_post,
    prefix='/post',
    tags=['Post section'],

)
app.include_router(
    likes.router_like,
    prefix='/like',
    tags=['Like section'],

)