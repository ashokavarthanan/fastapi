///////////////////////////////////////////////////////
#blog\schemas.py
#Added "ShowUserId" schema for id 

class ShowUserId(BaseModel):
    id: int
    class Config():
        orm_mode = True
        
///////////////////////////////////////////////////////
#user.py
#Added "showId" funtion for retrive users id 
def showId(email:str,db:Session):
    userId = db.query(models.User.id).filter(models.User.email == email).first()
    if userId is None:
        return null
    return userId

///////////////////////////////////////////////////////
# repository\blog.py
# Changed get_all to New CODE
def get_all(userid:int,db: Session):
    if userid is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Blog not Found')
    blogs = db.query(models.Blog).filter(models.Blog.user_id == userid).all()
    return blogs

///////////////////////////////////////////////////////
# routers\blog.py
# Changed routers CODE
@router.get('/',status_code=200)
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    userid = user.showId(current_user,db).id
    return blog.get_all(userid,db)



