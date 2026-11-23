class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, prioridade="Média"):
        tarefa = {
            "id": len(self.tarefas) + 1,
            "titulo": titulo,
            "prioridade": prioridade,
            "status": "A Fazer"
        }
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def atualizar_status(self, tarefa_id, novo_status):
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                tarefa["status"] = novo_status
                return True
        return False

    def deletar_tarefa(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                self.tarefas.remove(tarefa)
                return True
        return False