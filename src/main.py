from fastapi import FastAPI

app = FastAPI()

http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Olá Mundo"}

#http://127.0.0.1:8000/teste1
@app.get('/teste1')
async def funcaoteste():
    return {'Teste deu certo!!!'}

