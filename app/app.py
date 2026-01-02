from fastapi import FastAPI, HTTPException

app = FastAPI()

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
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
            raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)