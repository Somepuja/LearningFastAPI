from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

@app.get("/FirstPage/{a}/{b}")
def firstfunc(a,b):
    addition = int(a)+int(b)
    return addition


@app.post("/SecondPage")
def secondfunc(a:int,b:int) -> int:
    addition = a+b
    return addition

class InputModel(BaseModel):
    a : float
    b : int | float
    c : datetime.datetime = "2024-03-06T00:07:08"

@app.post("/ThirdPage")
def thirdfunc(inputmodel : InputModel):
    addition = inputmodel.a + inputmodel.b
    return {"addition":addition,"date":inputmodel.c}

