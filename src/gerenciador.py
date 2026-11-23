class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo):
        if not titulo:
            raise ValueError("O título da tarefa não pode estar vazio.")
        tarefa = {"titulo": titulo, "concluida": False}
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def filtrar_por_status(self, concluida):
        return [t for t in self.tarefas if t["concluida"] == concluida]