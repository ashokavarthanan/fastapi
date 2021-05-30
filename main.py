from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Ashok'}}

@app.get('/shop')
def shop(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return  {'data': {f'{limit} published page'}}
    else:
        return  {'data': {f'{limit} page'}}

@app.get('/shop/{id}')
def shop(id):
    return  {'data': {id: 'Ashok'}}


@app.get('/blog/unpublished')
def unpublished():
    return  {'data': 'all unpublished'}


@app.get('/blog/{id}/comments')
def shop(id: int,limit=10):
    #return limit
    return  {'data': {'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is Created with title as {blog.title}"}

# if __name__ == '__main__':
#     uvicorn.run(app,host="127.0.0.1", port=9000)