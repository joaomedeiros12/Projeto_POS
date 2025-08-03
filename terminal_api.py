import requests
import json
from datetime import timedelta

BASE_URL = "http://127.0.0.1:8000"  # Altere conforme necessário

def tratar_resposta(resposta):
    if resposta.status_code in [200, 201]:
        print("Sucesso:")
        print(json.dumps(resposta.json(), indent=2, ensure_ascii=False))
    else:
        print(f"Erro {resposta.status_code}:")
        print(resposta.text)

# FILMES
def listar_filmes():
    try:
        resposta = requests.get(f"{BASE_URL}/filmes")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao listar filmes:", e)

def criar_filme():
    try:
        dados = {
            "id": 0,  
            "titulo": input("Título: "),
            "genero": input("Gênero: "),
            "duracao": input("Duração (HH:MM:SS): "),
            "classificacao": input("Classificação: "),
            "sinopse": input("Sinopse: "),
            "diretor": input("Diretor: "),
            "elenco": input("Elenco (separado por vírgula): ").split(","),
            "ano": input("Ano (YYYY-MM-DD): "),
            "url_trailer": input("URL do trailer (opcional): ") or None,
            "url_imagem": input("URL da imagem (opcional): ") or None,
            "status": input("Status (ex: ativo, inativo): ") 
        }

        resposta = requests.post(f"{BASE_URL}/filmes", json=dados)
        tratar_resposta(resposta)

    except Exception as e:
        print("Erro ao criar filme:", e)


# SALAS
def listar_salas():
    try:
        resposta = requests.get(f"{BASE_URL}/salas")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao listar salas:", e)

    

def criar_sala():
    try:
        dados = {
            "nome": input("Nome da sala: "),
            "capacidade": int(input("Capacidade: "))
        }
        resposta = requests.post(f"{BASE_URL}/salas", json=dados)
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao criar sala:", e)

# SESSÕES
def listar_sessoes():
    try:
        resposta = requests.get(f"{BASE_URL}/sessoes")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao listar sessões:", e)

def criar_sessao():
    try:
        filme_id = int(input("ID do filme: "))
        sala_id = int(input("ID da sala: "))
        data = input("Data (YYYY-MM-DD): ")
        horario_inicio = input("Horário de início (HH:MM): ")
        duracao = input("Duração (HH:MM:SS): ")
        preco = float(input("Preço: "))
        tipo_exibicao = input("Tipo de exibição: ")
        status = input("Status: ")

        payload = {
            "filme_id": filme_id,
            "sala_id": sala_id,
            "data": data,
            "horario_inicio": horario_inicio,
            "duracao": duracao,
            "preco": preco,
            "tipo_exibicao": tipo_exibicao,
            "status": status
        }

        resposta = requests.post(f"{BASE_URL}/sessoes", json=payload)

        if resposta.status_code == 200 or resposta.status_code == 201:
            print("Sessão criada com sucesso!")
            print(resposta.json())
        else:
            print(f"Erro {resposta.status_code}:")
            print(resposta.text)
    except ValueError:
        print("Erro: Por favor, insira valores válidos para IDs, preço e datas.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

def atualizar_filme():
    try:
        filme_id = int(input("ID do filme a ser atualizado: "))
        dados = {
            "id": filme_id,
            "titulo": input("Novo título: "),
            "genero": input("Novo gênero: "),
            "duracao": input("Nova duração (HH:MM:SS): "),
            "classificacao": input("Nova classificação: "),
            "sinopse": input("Nova sinopse: "),
            "diretor": input("Novo diretor: "),
            "elenco": input("Novo elenco (separado por vírgula): ").split(","),
            "ano": input("Novo ano (YYYY-MM-DD): "),
            "url_trailer": input("Nova URL do trailer (opcional): ") or None,
            "url_imagem": input("Nova URL da imagem (opcional): ") or None,
            "status": input("Novo status: ")
        }
        resposta = requests.put(f"{BASE_URL}/filmes/{filme_id}", json=dados)
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao atualizar filme:", e)


def atualizar_sala():
    try:
        sala_id = int(input("ID da sala a ser atualizada: "))
        dados = {
            "id": sala_id,
            "nome": input("Novo nome da sala: "),
            "capacidade": int(input("Nova capacidade: "))
        }
        resposta = requests.put(f"{BASE_URL}/salas/{sala_id}", json=dados)
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao atualizar sala:", e)


def buscar_filme_por_id(filme_id):
    return requests.get(f"{BASE_URL}/filmes/{filme_id}").json()


def buscar_sala_por_id(sala_id):
    resposta = requests.get(f"{BASE_URL}/salas/{sala_id}")
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro ao buscar sala: {resposta.status_code} - {resposta.text}")
        return None


def deletar_filme():
    try:
        filme_id = int(input("ID do filme a ser deletado: "))
        resposta = requests.delete(f"{BASE_URL}/filmes/{filme_id}")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao deletar filme:", e)

def deletar_sala():
    try:
        sala_id = int(input("ID da sala a ser deletada: "))
        resposta = requests.delete(f"{BASE_URL}/salas/{sala_id}")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao deletar sala:", e)

def deletar_sessao():
    try:
        sessao_id = int(input("ID da sessão a ser deletada: "))
        resposta = requests.delete(f"{BASE_URL}/sessoes/{sessao_id}")
        tratar_resposta(resposta)
    except Exception as e:
        print("Erro ao deletar sessão:", e)
        

# MENU
def menu():
    while True:
        print("\nSistema de Gerenciamento de Filmes")
        print("1. Listar filmes")
        print("2. Criar filme")
        print("3. Atualizar filme")
        print("4. Deletar filme")
        print("5. Listar salas")
        print("6. Criar sala")
        print("7. Atualizar sala")
        print("8. Deletar sala")
        print("9. Listar sessões")
        print("10. Criar sessão")
        print("11. Atualizar sessão")
        print("12. Deletar sessão")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_filmes()
        elif opcao == "2":
            criar_filme()
        elif opcao == "3":
            atualizar_filme()
        elif opcao == "4":
            deletar_filme()
        elif opcao == "5":
            listar_salas()
        elif opcao == "6":
            criar_sala()
        elif opcao == "7":
            atualizar_sala()
        elif opcao == "8":
            deletar_sala()
        elif opcao == "9":
            listar_sessoes()
        elif opcao == "10":
            criar_sessao()
        elif opcao == "11":
            deletar_sessao()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
