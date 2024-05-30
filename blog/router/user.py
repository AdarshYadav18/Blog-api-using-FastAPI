from typing import List
from fastapi import FastAPI , Depends ,status ,Response ,HTTPException
import schemas
import models
import hashing
from database import engine  , get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter
from repository import user
import oauth2

router=APIRouter(
    prefix="/user",
    tags=['user']
)



@router.post('/',response_model=schemas.Showuser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)
    

@router.get('/{id}',response_model=schemas.Showuser)
def show_user(id, response:Response,db:Session=Depends(get_db),current_user:schemas.User =Depends(oauth2.get_current_user)):
    return user.show(id,db)

    