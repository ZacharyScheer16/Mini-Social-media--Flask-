import uvicorn

if __name__ == "__main__":     #running on local host anyone on ip address can access    #port 8080 is access
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True) #reload good for debugging

    