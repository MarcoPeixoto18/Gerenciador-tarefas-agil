class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, prioridade="Média"):
        if not titulo:
            raise ValueError("O título da tarefa não pode estar vazio.")
        if prioridade not in ["Baixa", "Média", "Alta"]:
            raise ValueError("Prioridade inválida.")
        
        tarefa = {
            "titulo": titulo, 
            "concluida": False,
            "prioridade": prioridade
        }
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def filtrar_por_status(self, concluida):
        return [t for t in self.tarefas if t["concluida"] == concluida]

    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                self.tarefas.remove(tarefa)
                return True
        raise ValueError("Tarefa não encontrada.")