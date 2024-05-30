from typing import List
from fastapi import FastAPI , Depends ,status ,Response ,HTTPException
import schemas
import models
import hashing
from database import engine  , get_db
from sqlalchemy.orm import Session


def create(request:schemas.User,db:Session):
    new_user=models.User(name=request.name ,email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with this id {id} is not available')
    return user