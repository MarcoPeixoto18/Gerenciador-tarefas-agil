from src.gerenciador import GerenciadorDeTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.adicionar_tarefa("Estudar Git", prioridade="Alta")
    assert len(gerenciador.listar_tarefas()) == 1
    assert tarefa["titulo"] == "Estudar Git"
    assert tarefa["prioridade"] == "Alta"

def test_atualizar_status():
    gerenciador = GerenciadorDeTarefas()
    gerenciador.adicionar_tarefa("Fazer trabalho")
    gerenciador.atualizar_status(1, "Concluído")
    assert gerenciador.listar_tarefas()[0]["status"] == "Concluído"

def test_deletar_tarefa():
    gerenciador = GerenciadorDeTarefas()
    gerenciador.adicionar_tarefa("Tarefa temporária")
    gerenciador.deletar_tarefa(1)
    assert len(gerenciador.listar_tarefas()) == 0