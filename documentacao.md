# Documentação do Projeto: Projeto de Gerenciamento de Cinema 

## 1. Visão Geral

**Tecnologia Utilizada:**

- Python  
- FastAPI  
- Uvicorn  
  

**Descrição:**  

**Gerenciador de cinema**

Este projeto é um sistema básico para gerenciar salas e sessões de cinema, desenvolvido usando FastAPI, uma biblioteca Python para criar APIs de forma rápida e fácil.

Ele permite cadastrar, atualizar, visualizar e excluir salas e sessões, com controle automático dos IDs para facilitar o uso. As sessões têm informações sobre a sala onde acontecem e a duração do filme.

**Objetivo:**  
Desenvolver uma API RESTful simples para gerenciamento de cinema que permita controlar salas e sessões, facilitando o cadastro, atualização, consulta e exclusão dessas informações, utilizando FastAPI.

---

## 2. Descrição Detalhada do Projeto

**O que é o projeto?**

Este projeto consiste no desenvolvimento de uma API RESTful para o gerenciamento de um cinema, utilizando a linguagem Python com o framework FastAPI. A aplicação tem como objetivo permitir que um administrador possa realizar operações como o cadastro, edição, listagem e exclusão de filmes, salas e sessões.

A API foi estruturada com foco na simplicidade e organização, permitindo testes e integração com interfaces futuras e o projeto está dividido em arquivos separados para melhor organização do código, como modelos (`models.py`), rotas da API (`api.py`) e inicialização (`main.py`).

Além das funcionalidades básicas de CRUD, o sistema está preparado para ser estendido com autenticação, filtros, relatórios e futuras integrações com bancos de dados e interfaces gráficas.

### 2.1 Funcionalidades Principais

### 2.1 Funcionalidades Principais

- **Funcionalidade 01: Login de Administrador**  
  Permitir que um administrador faça login com nome de usuário e senha. (RF001)

- **Funcionalidade 02: Recuperação de Senha**  
  Disponibilizar um mecanismo para recuperação de senha por parte do administrador. (RF002)

- **Funcionalidade 03: Controle de Acesso**  
  Garantir que apenas administradores autenticados possam acessar as funcionalidades de gerenciamento. (RF003)

- **Funcionalidade 04: Cadastrar Filme**  
  Permitir o cadastro de novos filmes com as seguintes informações: título, gênero, duração, classificação indicativa, sinopse, diretor, elenco principal, ano de lançamento, URL do trailer (opcional), URL da imagem do filme e status. (RF004)

- **Funcionalidade 05: Editar Filme**  
  Permitir a edição das informações de filmes já cadastrados. (RF005)

- **Funcionalidade 06: Listar Filmes**  
  Exibir uma lista de todos os filmes cadastrados com filtros por título, gênero e status, além de opções de ordenação. (RF006)

- **Funcionalidade 07: Detalhes do Filme**  
  Exibir todas as informações detalhadas de um filme selecionado. (RF007)

- **Funcionalidade 08: Excluir Filme**  
  Permitir a exclusão de filmes, alertando se estiverem associados a sessões futuras. (RF008)

- **Funcionalidade 09: Cadastrar Sala**  
  Permitir o cadastro de novas salas com nome/número, capacidade e descrição (opcional). (RF009)

- **Funcionalidade 10: Editar Sala**  
  Permitir a edição das informações das salas cadastradas. (RF010)

- **Funcionalidade 11: Listar Salas**  
  Exibir uma lista com todas as salas cadastradas. (RF011)

- **Funcionalidade 12: Excluir Sala**  
  Permitir a exclusão de salas, alertando se estiverem associadas a sessões futuras. (RF012)

- **Funcionalidade 13: Cadastrar Sessão**  
  Permitir o cadastro de sessões informando o filme, sala, data, horário de início, preço, tipo de exibição e status da sessão. (RF013)

- **Funcionalidade 14: Editar Sessão**  
  Permitir a edição das informações de sessões já cadastradas. (RF014)

- **Funcionalidade 15: Listar Sessões**  
  Exibir uma lista com todas as sessões, com filtros por filme, sala, data e status. (RF015)

- **Funcionalidade 16: Detalhes da Sessão**  
  Exibir todos os detalhes de uma sessão, incluindo o filme e a sala associados. (RF016)

- **Funcionalidade 17: Excluir Sessão**  
  Permitir a exclusão de sessões cadastradas. (RF017)

- **Funcionalidade 18: Relatório de Filmes por Status**  
  Gerar um relatório listando os filmes de acordo com seu status (Em cartaz, Em breve, Arquivado). (RF018)

- **Funcionalidade 19: Relatório de Sessões Futuras**  
  Gerar um relatório com sessões futuras, com filtros por data e filme. (RF019)

- **Funcionalidade 20: Consultar Sessões por Filme**  
  Permitir a consulta de todas as sessões relacionadas a um filme específico. (RF020)

- **Funcionalidade 21: Consultar Sessões por Sala**  
  Permitir a consulta de todas as sessões agendadas para uma sala específica. (RF021)


### 2.2 Arquitetura do Código


Projeto_POS/
├── main.py            # Ponto de entrada (inicialização)
├── api.py             # Lógica da API 
├── models.py          # Modelos com Pydantic


---

## 3. Etapas de Entrega (Cronograma Detalhado)

* **Etapa 1:** 24/04 - Definição do layout de usabilidade  
  Planejamento da estrutura visual e organização lógica da API, considerando a experiência de uso por parte do desenvolvedor (rotas intuitivas, organização dos dados e respostas claras).

* **Etapa 2:** 07/05 - Definição dos requisitos  
  Levantamento dos requisitos funcionais e não funcionais, definição dos módulos da aplicação (filmes, salas, sessões, etc.) e escopo das funcionalidades principais.

* **Etapa 3:** 19/05 - Implementação das rotas 
  Desenvolvimento inicial das rotas HTTP com FastAPI, incluindo os endpoints básicos para consulta e cadastro de dados (GET e POST).

* **Etapa 4:** 28/05 - Implementação de funcionalidades como PUT e DELETE
  Adição de funcionalidades de atualização e exclusão de dados (PUT e DELETE), com tratamento de erros e verificação de integridade.

* **Etapa 5:** 01/06 - Estruturação da documentação para entrega  
  Organização da documentação do projeto, incluindo estrutura de diretórios, descrição das funcionalidades, objetivos, requisitos e cronograma para apresentação final.
