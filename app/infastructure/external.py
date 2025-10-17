from pydantic import BaseModel


class CatFact(BaseModel):
    fact: str
    length: int
