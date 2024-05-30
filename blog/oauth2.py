from typing import Annotated
from fastapi import Depends, HTTPException, status
import jwt_token
import schemas
import models
from fastapi.security import OAuth2PasswordBearer



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def get_current_user(token:str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        return jwt_token.verifyToken(token,credentials_exception)

        

# @app.get("/users/me", response_model=dict)
# async def read_users_me(current_user: dict = Depends(get_current_user)):
#     return current_user
