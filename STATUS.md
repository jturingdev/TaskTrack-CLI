# 📊 Status do Projeto - Task Tracker CLI

**Estado Atual:** Desenvolvimento Inicial (Preparação da v0.1)
**Foco da Sprint Atual:** Estruturação da arquitetura base e implementação do MVP usando persistência em JSON.

## Tarefas Ativas
- [ ] Configurar ambiente virtual e instalar dependências (Click, Textual, Sentry-SDK).
- [ ] Definir a entidade `Task` na camada de Domínio.
- [ ] Criar a interface do Repositório (Abstract Base Class).
- [ ] Implementar a persistência com `json_repo.py`.
- [ ] Desenvolver os comandos básicos do CLI com Click.

## Decisões Arquiteturais Recentes
* **Padrão de Repositório:** Adotado para permitir a futura transição de JSON para SQLAlchemy/Redis sem alterar as regras de negócio.
* **Observabilidade:** Sentry adicionado desde o dia zero para rastreamento de exceções e monitorização.