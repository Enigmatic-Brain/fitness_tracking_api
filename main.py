from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
class register_schema(BaseModel):
    username: str
    email: str
    password: str
    phone_number: Optional[int] = None
    
users = []

app = FastAPI()

def find_user(id:int):
    for dict in users:
        if dict['id']==id:
            return dict
    

@app.get("/")
def welcome_message():
    return {"Message:", "Welcome to my Fitness API"}


@app.post("/users/registers")
def user_registration(info: register_schema):
    info_dict = info.model_dump()
    info_dict['id']=randrange(1, 100000000)
    users.append(info_dict)
    return {"message": "Registration Successful!",
            "Information": info_dict}

    
@app.get("/users/{id}")
def user_info(id:int):
    user_details = find_user(id)
    if not user_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} not found.")
    return {"user details": user_details}
    
# 