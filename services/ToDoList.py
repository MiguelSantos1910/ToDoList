from models import Tarefa
class ToDoList:
    def __init__(self):
        self.tarefasPendentes = []
        self.tarefasConcluidas = []
        self.tarefasRemovidas = []
    
    def adicionar(self, titulo, prioridade, data, hora):
        tarefa = Tarefa(titulo = titulo, prioridade = prioridade, data = data, hora = data)
        self.tarefasPendentes.append(tarefa)
        self.proximo_id += 1
        return tarefa

    def concluir_tarefa(self, id):
        for tarefa in self.tarefasPendentes:
            if tarefa.id == id:
                tarefa.concluir()
            return None
        self.tarefasPendentes.remove(tarefa)
        self.tarefasConcluidas.append(tarefa)
        return tarefa

    def remover(self, id):
        for lista in (self.tarefasPendentes, self.tarefasConcluidas):
            for tarefa in lista:
                if tarefa.id == id:
                    lista.remove(tarefa)
        self.tarefasRemovidas.append(tarefa)
        return

    def listarTarefasPendentes(self):
        for tarefas in self.tarefasPendentes:
            print(f"{tarefas.id} | {tarefas.titulo} | {tarefas.prioridade}")