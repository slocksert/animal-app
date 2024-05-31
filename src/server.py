from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class Animal(BaseModel):
    id: str | None = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get('/animais')
async def visualizar():
    return banco

@app.post('/animais')
async def adicionar(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return {'dados': f'Nome:{animal.nome} Idade:{animal.idade} Sexo: {animal.sexo} Cor: {animal.cor}'}

@app.get('/animais/{animal_id}')
async def visualizar_id(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return { 'erro': 'Animal não localizado'}

@app.delete('/animais/{animal_id}')
async def delete_id(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            banco.remove(animal)
            return { "mensagem": f"{animal_id} foi removido!"}

if __name__ == '__main__':    
    uvicorn.run(
        "server:app",
        host='localhost',
        port=8000,
        reload=True,
        server_header=0
    )