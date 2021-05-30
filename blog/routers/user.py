from fastapi import APIRouter, Depends, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from .repository import user
get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post('/',response_model=schemas.ShowUser)
def creste_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowUser)
def get_user(id:int,response:Response,db: Session = Depends(get_db)):
    return user.show(id,db)