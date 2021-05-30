from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null
from ... import models, schemas, hashing


def create(request: schemas.User,db: Session):
    new_user = models.User(user=request.user,email=request.email,password=hashing.hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'User id {id} is not available')
    return user

def showId(email:str,db:Session):
    userId = db.query(models.User.id).filter(models.User.email == email).first()
    if userId is None:
        return null
    return userId