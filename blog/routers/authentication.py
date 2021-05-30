from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from .. import database,models,token
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import hash

router = APIRouter(
    #  prefix="/user",
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'User id {request.username} is not available')
    if not hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Incorrct Password')

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}