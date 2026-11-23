from src.gerenciador import GerenciadorTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Estudar Python")
    assert len(gerenciador.listar_tarefas()) == 1
    assert gerenciador.listar_tarefas()[0]["titulo"] == "Estudar Python"
    assert gerenciador.listar_tarefas()[0]["concluida"] is False

def test_adicionar_tarefa_vazia():
    gerenciador = GerenciadorTarefas()
    try:
        gerenciador.adicionar_tarefa("")
    except ValueError as e:
        assert str(e) == "O título da tarefa não pode estar vazio."