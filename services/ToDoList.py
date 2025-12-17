from models import Tarefa
class ToDoList:
    def __init__(self):
        self.tarefasPendentes = []
        self.tarefasConcluidas = []
        self.tarefasRemovidas = []
    
    def adicionar(self, tarefa):
        self.tarefasPendentes.append(tarefa)

    def concluir_tarefa(self, id):
        for tarefa in self.tarefasPendentes:
            if tarefa.id == id:
                tarefa.concluir()
            self.tarefasPendentes.remove(tarefa)
            self.tarefasConcluidas.append(tarefa)
            break

    def remover(self, id):
        for lista in (self.tarefasPendentes, self.tarefasConcluidas):
            for tarefa in lista:
                if tarefa.id == id:
                    lista.remove(tarefa)
        self.tarefasRemovidas.append(tarefa)
        return

    def listarTarefasPendentes(self):
        for tarefa in self.tarefasPendentes:
            print(f"{tarefa.id} | {tarefa.titulo} | {tarefa.prioridade}")