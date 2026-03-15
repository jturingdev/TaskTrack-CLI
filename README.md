📝 Task Tracker CLI

# O Task Tracker CLI é uma aplicação de linha de comando robusta para gestão de tarefas, desenvolvida em Python. 
    O projeto foca na organização eficiente de afazeres, permitindo o rastreio completo desde a criação até à conclusão, com persistência de dados local.

# 🚀 Funcionalidades

- Gestão Completa (CRUD): Adicione, visualize, atualize e remova tarefas de forma intuitiva.
- Identificação Única: Cada tarefa recebe um UUID (Universally Unique Identifier) para garantir que não haja conflitos.
- Persistência Automática: Os dados são guardados em tempo real num ficheiro tasks.json.
- Categorização e Status: Organize o seu fluxo com categorias (Work, School, Personal) e estados (Todo, Progress, Done).
- Visualização Estruturada: Integração com a biblioteca Pandas para exibir as suas tarefas de forma organizada.
- Busca Flexível: Atualize ou remova tarefas utilizando tanto o ID quanto o Título.

# 🛠️ Tecnologias Utilizadas

- Python 3.13+: Linguagem base.
- JSON: Formato para armazenamento de dados.
- Logging: Sistema de registo de erros e eventos para maior fiabilidade.
- UUID: Para geração de chaves primárias únicas.

# Metodologia Utilizada
 - SRP - Single Responsability Principle
 - Separation of Concerns(SOC)

# Estruturas de Dados Utilizadas:
- Stack
- Queue

# 📋 Como Utilizar
Pré-requisitos

# Execução:
- Clone o repositório. 
- Navegue até à pasta do projeto. 
- Execute o comando:
- Bash: python install -e .

# Menu de Opções
## Ao iniciar, terá acesso ao seguinte menu:
- Add Task: [task-cli add title description category author status priority term]
- List Tasks: [task-cli list all]
- List Task by status: [task-cli list [done or progress] ]
- Mark Status: [task-cli id [done or progress]]
- Update: [id --title --description --category --author --status --priority --term]
- Delete: [id]

# 📂 Estrutura de Dados
## As tarefas são armazenadas no formato:
JSON
{
    "id": "id como numero inteiro"
    "uuid": "uuid-gerado-automaticamente",
    "title": "Exemplo de Tarefa",
    "description": "Detalhes da atividade",
    "author": "Your name"
    "category": WORK,
    "status": TODO,
    "priority": NORMAL,
    "term": TODAY,
    "createdAt": "dd/mm/aaaa hh:mm",
    "updateAt": "dd/mm/aaaa hh:mm"
}

## 👨‍💻 Autor
Desenvolvido como projeto prático para consolidar conceitos de manipulação de ficheiros, Programação Orientada a Objetos (POO) e CLI em Python.