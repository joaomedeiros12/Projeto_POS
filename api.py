from fastapi import APIRouter, HTTPException
from typing import List
from models import Filme, Assento, Sala, Sessao

router = APIRouter()

filmes: List[Filme] = []
assentos: List[Assento] = []
salas: List[Sala] = []
sessoes: List[Sessao] = []

@router.get("/filmes", response_model=List[Filme])
def exibir_filmes():
    return filmes

@router.get("/filmes/{id}", response_model=Filme)
def detalhar_filme(id: int):
    for filme in filmes:
        if filme.id == id:
            return filme
    raise HTTPException(404, "Filme não localizado ou não cadastrado.")

@router.post("/filmes", response_model=Filme)
def criar_filme(filme: Filme):
    novo_id = len(filmes) + 1
    novo_filme = Filme(
        id=novo_id,
        titulo=filme.titulo,
        duracao=filme.duracao,
        ano=filme.ano,
        sinopse=filme.sinopse
    )
    filmes.append(novo_filme)
    return novo_filme

@router.put("/filmes/{id}", response_model=Filme)
def atualizar_filme(id: int, filme: Filme):
    for i, f in enumerate(filmes):
        if f.id == id:
            filme.id = id
            filmes[i] = filme
            return filme
    raise HTTPException(status_code=404, detail="Filme não encontrado.")

@router.delete("/filmes/{id}", response_model=Filme)
def deletar_filme(id: int):
    for i, filme in enumerate(filmes):
        if filme.id == id:
            return filmes.pop(i)
    raise HTTPException(status_code=404, detail="Filme não encontrado.")

@router.get("/salas", response_model=List[Sala])
def visualizar_salas():
    return salas

@router.post("/salas", response_model=Sala)
def criar_sala(sala_input: Sala):
    novo_id = (salas[-1].id + 1) if salas else 1
    nova_sala = Sala(id=novo_id, nome=sala_input.nome, capacidade=sala_input.capacidade)
    salas.append(nova_sala)
    return nova_sala

@router.put("/salas/{id}", response_model=Sala)
def atualizar_sala(id: int, sala_atualizada: Sala):
    for i, s in enumerate(salas):
        if s.id == id:
            sala_atualizada.id = id
            salas[i] = sala_atualizada
            return sala_atualizada
    raise HTTPException(status_code=404, detail="Sala não encontrada.")

@router.delete("/salas/{id}", response_model=Sala)
def deletar_sala(id: int):
    for i, s in enumerate(salas):
        if s.id == id:
            return salas.pop(i)
    raise HTTPException(status_code=404, detail="Sala não encontrada.")

@router.get("/sessoes", response_model=List[Sessao])
def listar_sessoes():
    return sessoes

@router.get("/sessoes/{id}", response_model=Sessao)
def visualizar_sessao(id: int):
    for sessao in sessoes:
        if sessao.id == id:
            return sessao
    raise HTTPException(status_code=404, detail="Sessão não encontrada.")

@router.post("/sessoes", response_model=Sessao)
def criar_sessao(sessao_input: Sessao):
    novo_id = (sessoes[-1].id + 1) if sessoes else 1
    nova_sessao = Sessao(id=novo_id, sala=sessao_input.sala, duracao=sessao_input.duracao)
    sessoes.append(nova_sessao)
    return nova_sessao

@router.put("/sessoes/{id}", response_model=Sessao)
def atualizar_sessao(id: int, sessao_input: Sessao):
    for i, s in enumerate(sessoes):
        if s.id == id:
            sessoes[i] = Sessao(id=id, sala=sessao_input.sala, duracao=sessao_input.duracao)
            return sessoes[i]
    raise HTTPException(status_code=404, detail="Sessão não encontrada.")

@router.delete("/sessoes/{id}", response_model=Sessao)
def deletar_sessao(id: int):
    for i, s in enumerate(sessoes):
        if s.id == id:
            return sessoes.pop(i)
    raise HTTPException(status_code=404, detail="Sessão não encontrada.")
