📝 Task Tracker CLI

O Task Tracker CLI é uma aplicação de linha de comando robusta para gestão de tarefas, desenvolvida em Python. O projeto foca na organização eficiente de afazeres, permitindo o rastreio completo desde a criação até à conclusão, com persistência de dados local.
🚀 Funcionalidades

- Gestão Completa (CRUD): Adicione, visualize, atualize e remova tarefas de forma intuitiva.
- Identificação Única: Cada tarefa recebe um UUID (Universally Unique Identifier) para garantir que não haja conflitos.
- Persistência Automática: Os dados são guardados em tempo real num ficheiro tasks.json.
- Categorização e Status: Organize o seu fluxo com categorias (Work, School, Personal) e estados (Todo, Progress, Done).
- Visualização Estruturada: Integração com a biblioteca Pandas para exibir as suas tarefas de forma organizada.
- Busca Flexível: Atualize ou remova tarefas utilizando tanto o ID quanto o Título.

🛠️ Tecnologias Utilizadas

- Python 3.13+: Linguagem base.
- JSON: Formato para armazenamento de dados.
- Pandas: Utilizado para a manipulação e exibição de tabelas de dados.
- Logging: Sistema de registo de erros e eventos para maior fiabilidade.
- UUID: Para geração de chaves primárias únicas.

📋 Como Utilizar
Pré-requisitos

Certifique-se de ter o Python e o Pandas instalados:
    Bash: pip install pandas

Execução:

- Clone o repositório. 
- Navegue até à pasta do projeto. 
- Execute o comando:
- Bash: python app.py

Menu de Opções

Ao iniciar, terá acesso ao seguinte menu:

- Add Task: Cria uma nova tarefa solicitando título, descrição, categoria e autor.
- List Tasks: Exibe todas as tarefas guardadas no sistema.
- Update: Permite modificar campos específicos (Título, Descrição, Status, etc.) de uma tarefa existente.
- Delete: Remove uma tarefa permanentemente através do ID ou Título.
- Exit (q): Encerra o programa em segurança.

📂 Estrutura de Dados

As tarefas são armazenadas no formato:
JSON

{
    "id": "uuid-gerado-automaticamente",
    "title": "Exemplo de Tarefa",
    "description": "Detalhes da atividade",
    "category": "WORK",
    "status": "todo",
    "createdAt": "dd/mm/aaaa hh:mm",
    "updateAt": "dd/mm/aaaa hh:mm"
}

👨‍💻 Autor

Desenvolvido como projeto prático para consolidar conceitos de manipulação de ficheiros, Programação Orientada a Objetos (POO) e CLI em Python.