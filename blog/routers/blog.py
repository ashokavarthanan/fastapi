from fastapi import APIRouter, Depends, status, Response
from typing import List

from sqlalchemy.sql.expression import null
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from .repository import blog,user
get_db = database.get_db
router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/',status_code=200)
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    userid = user.showId(current_user,db).id
    # if userid is None:
    #     return "{Blog not Found}"
    # return user_id
    return blog.get_all(userid,db)

# def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     # return schemas.User
#     return blog.get_all(db)

# @router.get('/',status_code=200,response_model=List[schemas.ShowBlog])
# def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,response:Response,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)