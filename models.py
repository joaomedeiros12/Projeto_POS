from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date, time, timedelta

class Filme(BaseModel):
    id: int
    titulo: str
    genero: str
    duracao: str
    classificacao: str
    sinopse: str
    diretor: str
    elenco: List[str]
    ano: date
    url_trailer: Optional[HttpUrl] = None
    url_imagem: Optional[HttpUrl] = None
    status: str

class Sala(BaseModel):
    id: int
    nome: str
    capacidade: int

class Sessao(BaseModel):
    id: Optional[int]
    filme_id: int
    sala_id: int
    data: date
    horario_inicio: time
    duracao: timedelta  
    preco: float
    tipo_exibicao: str
    status: str


class FilmeCreate(BaseModel):
    titulo: str
    genero: str
    duracao: str
    classificacao: str
    sinopse: str
    diretor: str
    elenco: List[str]
    ano: date
    url_trailer: Optional[HttpUrl] = None
    url_imagem: Optional[HttpUrl] = None
    status: str

class SalaCreate(BaseModel):
    nome: str
    capacidade: int

class SessaoCreate(BaseModel):
    filme_id: int
    sala_id: int
    data: date
    horario_inicio: time
    duracao: str
    preco: float
    tipo_exibicao: str
    status: str
