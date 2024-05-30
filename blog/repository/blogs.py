from typing import List
from fastapi import FastAPI , Depends ,status ,Response ,HTTPException
import schemas
import models
import hashing
from database import engine , SessionLocal , get_db
from sqlalchemy.orm import Session
from router import authentication
import oauth2



def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs



def create(request:schemas.Blog,db:Session,current_user):
    new_blog=models.Blog(title=request.title, body=request.body,user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)   
    return new_blog


def destroy(id,db:Session):
    blog= db.query(models.Blog).filter(models.Blog.id==id)
   
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f' Blog with id {id} not found')
        
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:schemas.Blog,db:Session):
    blog= db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f' Blog with id {id} not found')

    blog.update(request.dict())
    db.commit()
    return 'Updated'

def show(id:int, db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with this id {id} is not available')
    return blog
