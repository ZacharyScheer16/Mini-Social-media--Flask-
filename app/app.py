from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"} #json -> java script object notation (USE DICT) valid python dict = valid json
