
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI()

# Temporary database
users_db = []

# Define the structure of a user
class User(BaseModel):
    name: str
    age: int


# Home endpoint
@app.get("/")
def home():
    return {"message": "My FastAPI backend is working!"}


# GET: Fetch all users
@app.get("/users")
def get_users():
    return users_db


# POST: Create a new user
@app.post("/users", status_code=201)
def create_user(user: User):

    new_user = {
        "id": len(users_db) + 1,
        "name": user.name,
        "age": user.age
    }

    users_db.append(new_user)

    return new_user
