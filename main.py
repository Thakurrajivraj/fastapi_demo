from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hello World from FastAPI!"}   
@app.post("/users")
def read_users(user:dict):
    return {"message": "User created successfully", "user": user}