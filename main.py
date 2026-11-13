from typing import Optional
import random
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

my_posts=[{"title":"title of post 1", "content":"content of post 1","id":1},
          {"title":"title of post 2", "content":"content of post 2","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

@app.get("/")
async def root():
    return "Hello World"

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(Post:post):
    Post_dict=Post.dict()
    Post_dict["id"]=random.randint(0, 10000000)
    my_posts.append(Post_dict)
    print(Post)
    return {"data":Post_dict}

@app.get("/posts/{id}")
def get_post(id : int):                      #here you can declare the type so that the id in the path can be converted to an int
    return {"post id":find_post(int(id))}