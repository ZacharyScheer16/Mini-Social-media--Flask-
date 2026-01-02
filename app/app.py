from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, Form
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

'''
text_posts = {
    1: {"title": "Logistics Route Optimization", "content": "How to use AI to find the shortest delivery paths."},
    2: {"title": "FastAPI Performance Tips", "content": "Using asynchronous endpoints for high-concurrency APIs."},
    3: {"title": "Dockerizing Python Apps", "content": "A guide to creating slim Docker images with uv."},
    4: {"title": "Supply Chain Visibility", "content": "Tracking shipments in real-time across global borders."},
    5: {"title": "The Future of Warehousing", "content": "Automating pick-and-pack operations with robotics."},
    6: {"title": "Global Shipping Trends", "content": "How fuel prices are impacting international freight costs."},
    7: {"title": "Inventory Management 101", "content": "Best practices for maintaining stock levels in 2026."},
    8: {"title": "API Security Best Practices", "content": "Securing your FastAPI endpoints with OAuth2 and JWT."},
    9: {"title": "Sustainable Logistics", "content": "Reducing carbon footprints through electric delivery fleets."},
    10: {"title": "Microservices Architecture", "content": "Breaking down large logistics software into smaller services."}
}

@app.get("/posts") 
def get_all_posts(limit: int = None):
    if limit:
         return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
            raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

#POST endpoint
@app.post("/posts")
def create_post(post: PostCreate)-> PostResponse:     
     new_post = {"title": post.title, "content": post.content}
     text_posts[max(text_posts.keys()) + 1] = new_post
     return new_post
     
     
     ****demo code for in-memory storage
     '''

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="dummyurl",
        file_type='photo',
        file_name="dummy name"
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()] #result.all()
    post_data = []

    for post in posts:
        post_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })
    return {"posts": post_data}