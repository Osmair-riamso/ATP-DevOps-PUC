from random import randint
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Estudante(BaseModel):
    nome:str
    curso:str
    ativo:bool

#http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Olá Mundo"}

#http://127.0.0.1:8000/teste1
@app.get('/funcaoteste')
async def funcaoteste():
    return {"Teste": True, "num_alatorio": random.randint(a: 0, b: 20000)}



