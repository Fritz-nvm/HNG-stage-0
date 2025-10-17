from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    stack: str


class Response(BaseModel):
    status: str
    user: User
    timestamp: str
    cat_fact: str
