from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null
from ... import models, schemas


# def get_all(current_user,db: Session):
#     blogs = db.query(models.Blog).all()
#     return blogs

# def delete(id:int,db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail= f'Blog id {id} is not Found')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {'Deleted'}

def get_all(userid:int,db: Session):
    if userid is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Blog not Found')
    blogs = db.query(models.Blog).filter(models.Blog.user_id == userid).all()
    return blogs

def create(request: schemas.Blog,db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Blog id {id} is not Found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'Deleted'}

def update(id:int,request: schemas.Blog,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Blog id {id} is not Found')
    blog.update({"title": request.title,"body": request.body})
    db.commit()
    return "Updated"

def show(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Blog id {id} is not available')
    return blog