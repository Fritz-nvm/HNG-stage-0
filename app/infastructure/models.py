from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    stack: str


class Response(BaseModel):
    status: str
    timestamp: str
    cat_fact: str
