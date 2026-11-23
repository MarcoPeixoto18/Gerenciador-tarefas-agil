from src.gerenciador import GerenciadorTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Estudar Python")
    assert len(gerenciador.listar_tarefas()) == 1
    assert gerenciador.listar_tarefas()[0]["titulo"] == "Estudar Python"
    assert gerenciador.listar_tarefas()[0]["concluida"] is False
    assert gerenciador.listar_tarefas()[0]["prioridade"] == "Média"

def test_adicionar_tarefa_com_prioridade():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Projeto Urgente", "Alta")
    assert gerenciador.listar_tarefas()[0]["prioridade"] == "Alta"

def test_adicionar_tarefa_vazia():
    gerenciador = GerenciadorTarefas()
    try:
        gerenciador.adicionar_tarefa("")
    except ValueError as e:
        assert str(e) == "O título da tarefa não pode estar vazio."

def test_filtrar_por_status():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Tarefa 1")
    gerenciador.listar_tarefas()[0]["concluida"] = True
    
    pendentes = gerenciador.filtrar_por_status(False)
    concluidas = gerenciador.filtrar_por_status(True)
    
    assert len(pendentes) == 0
    assert len(concluidas) == 1
    assert concluidas[0]["titulo"] == "Tarefa 1"

def test_remover_tarefa():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Tarefa para apagar")
    assert len(gerenciador.listar_tarefas()) == 1
    
    gerenciador.remover_tarefa("Tarefa para apagar")
    assert len(gerenciador.listar_tarefas()) == 0

def test_atualizar_tarefa():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Tarefa Antiga", "Baixa")
    
    gerenciador.atualizar_tarefa("Tarefa Antiga", novo_titulo="Tarefa Nova", nova_prioridade="Alta")
    
    tarefa = gerenciador.listar_tarefas()[0]
    assert tarefa["titulo"] == "Tarefa Nova"
    assert tarefa["prioridade"] == "Alta"

def test_atualizar_tarefa_nao_encontrada():
    gerenciador = GerenciadorTarefas()
    try:
        gerenciador.atualizar_tarefa("Inexistente", novo_titulo="Novo")
    except ValueError as e:
        assert str(e) == "Tarefa não encontrada."