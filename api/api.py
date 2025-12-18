from fastapi import FastAPI
from services.Login import fazer_login
from services.ToDoList import ToDoList

app = FastAPI()
logado = fazer_login()
tarefas = ToDoList()

#---------Login-------------
@app.get("/")
def root():
    return ("Status: Api ativa!")

@app.post("/cadastrar-usuario")
def cadastro_usuario(nome: str, email: str, senha: str):
    return logado.cadastro(nome, email, senha)

@app.post('/login')
def login_usuario(email: str, senha: str):
    usuario =  logado.login(email, senha)

    if not usuario:
        return {"Erro: Login inválido!"}
    
    return usuario

#---------Tarefas-------------
@app.get("/tarefas-pendentes")
def pendentes():
    return tarefas.listarTarefasPendentes

@app.get("/tarefas-concluidas")
def concluidas():
    return tarefas.tarefasConcluidas

@app.get("/tarefas-removidas")
def removidas():
    return tarefas.tarefasRemovidas

@app.post("/concluir-tarefa")
def concluir(id: int):
    terminadas = tarefas.concluir_tarefa(id)

    if not terminadas:
        return {"Erro: Tarefa não encontrada!"}
    
    return terminadas

@app.post("/remover-tarefa")
def remove(id: int):
    excluidas = tarefas.remover(id)

    if not excluidas:
        return {"Erro: Tarefa não encontrada!"}
    
    return excluidas

@app.post("/criar-tarefa")
def criar(id: int, titulo: str, prioridade: str, data: str = None, hora: str = None):
    tarefa = tarefas.adicionar(id, titulo, prioridade, data, hora)

    if not tarefa:
        return {"Erro: Tarefa inválida!"}
    
    return tarefa
