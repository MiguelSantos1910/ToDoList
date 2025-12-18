class Tarefa:
    def __init__(self, id, titulo, prioridade='baixa', data=None, hora=None):
        self.id = id
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluido = False
        self.hora = hora
        self.data = data
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def atualizar(self, titulo=None, prioridade=None):
        if titulo:
            self.titulo = titulo
        if prioridade:
            self.prioridade = prioridade