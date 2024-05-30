from typing import List
from fastapi import FastAPI , Depends ,status ,Response ,HTTPException
import schemas
import models
import hashing
from database import engine , SessionLocal , get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter
from repository import blogs
import oauth2


router=APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.post('/' ,status_code=status.HTTP_201_CREATED)
def create(request :schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blogs.create(request, db,current_user)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blogs.get_all(db)

@router.get('/{id}' ,response_model=schemas.ShowBlog)
def show(id ,db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blogs.show(id,db)
    
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id ,db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blogs.destroy(id,db)
   

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blogs.update(id,request,db)
    

