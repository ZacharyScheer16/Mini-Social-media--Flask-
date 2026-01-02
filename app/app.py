from fastapi import FastAPI

app = FastAPI()

text_posts = {1: {"title": "First Post", "content": "This is the first post."}
              , 2: {"title": "Second Post", "content": "This is the second post."
                    }
              , 3: {"title": "Third Post", "content": "This is the third post."}
              }

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    return text_posts.get(id)