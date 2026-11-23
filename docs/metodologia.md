# Metodologia Ágil - Gerenciador de Tarefas

Este projeto utiliza princípios de metodologias ágeis (inspirado em Scrum/Kanban) para o planeamento e desenvolvimento iterativo.

## Backlog do Produto
- [x] Estrutura inicial do projeto e CI/CD
- [x] Funcionalidade de adicionar e listar tarefas
- [x] Filtro de tarefas por status (pendentes/concluídas)
- [x] Atribuição de níveis de prioridade
- [x] Funcionalidade de remover tarefas
- [ ] Funcionalidade de atualizar/editar tarefas (Próximo)

## Controle de Qualidade (CI/CD)
Cada alteração é testada automaticamente através do GitHub Actions utilizando `pytest` para garantir a estabilidade do código antes de chegar à branch principal (`main`).