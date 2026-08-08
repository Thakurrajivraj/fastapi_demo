from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hello World from FastAPI!"}   
@app.post("/users")
def read_users(user:dict):
    return {"message": "User created successfully", "user": user}
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "message": "User details retrieved successfully"}