from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class Operands(BaseModel):
    a: float
    b: float


router = APIRouter()


@router.post("/add")
def add(data: Operands):
    return {"result": data.a + data.b}


@router.post("/div")
def divide(data: Operands):
    if data.b == 0:
        raise HTTPException(400, "Division by zero")
    return {"result": data.a / data.b}
