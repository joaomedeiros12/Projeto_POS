from fastapi import APIRouter, HTTPException
from typing import List
from models import Filme, Sala, Sessao
from datetime import date, time, timedelta

router = APIRouter()

filmes: List[Filme] = []
salas: List[Sala] = []
sessoes: List[Sessao] = []

# Filmes
@router.get("/filmes", response_model=List[Filme])
def listar_filmes():
    return filmes

@router.get("/filmes/{filme_id}", response_model=Filme)
def obter_filme(filme_id: int):
    for filme in filmes:
        if filme.id == filme_id:
            return filme
    raise HTTPException(status_code=404, detail="Filme não encontrado")

@router.post("/filmes", response_model=Filme)
def criar_filme(filme: Filme):
    filme.id = max([f.id for f in filmes], default=0) + 1
    filmes.append(filme)
    return filme

@router.put("/filmes/{filme_id}", response_model=Filme)
def atualizar_filme(filme_id: int, novo: Filme):
    for i, filme in enumerate(filmes):
        if filme.id == filme_id:
            filmes[i] = novo
            return novo
    raise HTTPException(status_code=404, detail="Filme não encontrado")

@router.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int):
    for filme in filmes:
        if filme.id == filme_id:
            filmes.remove(filme)
            return {"mensagem": "Filme deletado"}
    raise HTTPException(status_code=404, detail="Filme não encontrado")


# Salas
@router.get("/salas", response_model=List[Sala])
def listar_salas():
    return salas

@router.get("/salas/{sala_id}", response_model=Sala)
def obter_sala(sala_id: int):
    for sala in salas:
        if sala.id == sala_id:
            return sala
    raise HTTPException(status_code=404, detail="Sala não encontrada")

@router.post("/salas", response_model=Sala)
def criar_sala(sala: Sala):
    sala.id = max([s.id for s in salas], default=0) + 1
    salas.append(sala)
    return sala

@router.put("/salas/{sala_id}", response_model=Sala)
def atualizar_sala(sala_id: int, nova: Sala):
    for i, sala in enumerate(salas):
        if sala.id == sala_id:
            salas[i] = nova
            return nova
    raise HTTPException(status_code=404, detail="Sala não encontrada")

@router.delete("/salas/{sala_id}")
def deletar_sala(sala_id: int):
    for sala in salas:
        if sala.id == sala_id:
            salas.remove(sala)
            return {"mensagem": "Sala deletada"}
    raise HTTPException(status_code=404, detail="Sala não encontrada")


# Sessões
@router.get("/sessoes", response_model=List[Sessao])
def listar_sessoes():
    return sessoes

@router.get("/sessoes/{sessao_id}", response_model=Sessao)
def obter_sessao(sessao_id: int):
    for sessao in sessoes:
        if sessao.id == sessao_id:
            return sessao
    raise HTTPException(status_code=404, detail="Sessão não encontrada")

@router.post("/sessoes", response_model=Sessao)
def criar_sessao(sessao: Sessao):
    sessao.id = max([s.id for s in sessoes], default=0) + 1  
    sessoes.append(sessao)
    return sessao

@router.put("/sessoes/{sessao_id}", response_model=Sessao)
def atualizar_sessao(
    sessao_id: int,
    filme_id: int,
    sala_id: int,
    data: date,
    horario_inicio: time,
    duracao: timedelta,
    preco: float,
    tipo_exibicao: str,
    status: str
):
    for i, s in enumerate(sessoes):
        if s.id == sessao_id:
            filme = next((f for f in filmes if f.id == filme_id), None)
            sala = next((s for s in salas if s.id == sala_id), None)
            if not filme or not sala:
                raise HTTPException(status_code=404, detail="Filme ou Sala não encontrados")

            nova_sessao = Sessao(
                id=sessao_id,
                filme=filme,
                sala=sala,
                data=data,
                horario_inicio=horario_inicio,
                duracao=duracao,
                preco=preco,
                tipo_exibicao=tipo_exibicao,
                status=status
            )
            sessoes[i] = nova_sessao
            return nova_sessao
    raise HTTPException(status_code=404, detail="Sessão não encontrada")

@router.delete("/sessoes/{sessao_id}")
def deletar_sessao(sessao_id: int):
    for sessao in sessoes:
        if sessao.id == sessao_id:
            sessoes.remove(sessao)
            return {"mensagem": "Sessão deletada"}
    raise HTTPException(status_code=404, detail="Sessão não encontrada")
