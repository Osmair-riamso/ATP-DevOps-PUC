import random
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
    return {"funcaoteste": True,"num_alatorio": random.randint(0,20000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante:Estudante):
    return estudante


@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante:int):
    return id_estudante > 0



