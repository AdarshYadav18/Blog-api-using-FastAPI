from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
import schemas
from typing import List,Annotated
from fastapi import FastAPI , Depends ,status ,Response ,HTTPException
import schemas
import models
from  hashing import Hash
from sqlalchemy.orm import Session
from database import engine , SessionLocal , get_db
import jwt_token 
router=APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()

    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invaild credentials')

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invaild Password')

    access_token =jwt_token.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

