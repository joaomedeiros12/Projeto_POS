from pydantic import BaseModel
from datetime import date, timedelta

class Administrador(BaseModel):
    email:str
    senha:str

class Assento(BaseModel):
    id:int
    fila:str
    coluna:int

class Sala(BaseModel):
    id: int
    nome: str
    capacidade: int

class Sessao(BaseModel):
    id: int
    sala: Sala
    duracao: timedelta

class Filme(BaseModel):
    id:int
    titulo:str
    ano:date
    sinopse:str
    duracao:timedelta

class Ingresso(BaseModel):
    id:int
    cpf_cli:int
    valor:int
    assento:Assento