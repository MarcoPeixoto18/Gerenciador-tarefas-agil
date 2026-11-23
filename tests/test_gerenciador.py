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

def test_filtrar_por_status():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Tarefa 1")
    # Simula marcar a primeira tarefa como concluída
    gerenciador.listar_tarefas()[0]["concluida"] = True
    
    pendentes = gerenciador.filtrar_por_status(False)
    concluidas = gerenciador.filtrar_por_status(True)
    
    assert len(pendentes) == 0
    assert len(concluidas) == 1
    assert concluidas[0]["titulo"] == "Tarefa 1"