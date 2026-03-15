# 📊 Status do Projeto - Task Tracker CLI

**Status:** Ativo
**Fase:** MVP Estabilizado (v1.0.0 lançada)
**Próxima Milestone:** v1.1
**Estado Atual:** Preparação para a v1.1 (Refatoração e Evolução de Ferramentas)
**Foco da Sprint Atual:** Evoluir a interface CLI (migração planeada para Click/Textual), adicionar observabilidade avançada com Sentry e solidificar a arquitetura de repositório.

## Tarefas Ativas
- [x] Definir a entidade `Task` na camada de Domínio (Implementado com UUID e Enums).
- [x] Implementar a persistência de dados com `json_repo.py`.
- [x] Desenvolver os comandos básicos do CLI (Implementado na v1.0 utilizando `argparse`).
- [ ] Configurar ambiente virtual e instalar novas dependências (Click, Textual, Sentry-SDK).
- [ ] Refatorar os comandos do CLI migrando de `argparse` para `Click`.
- [ ] Integrar Sentry-SDK para rastreamento de erros e exceções avançadas.

## Decisões Arquiteturais Recentes
* **Interface CLI (MVP vs Evolução):** A v1.0 foi construída com `argparse` por ser nativo do Python (zero dependências externas), validando a lógica de negócio. A migração para `Click` e `Textual` será feita na v1.1 para melhorar a experiência de desenvolvimento e do utilizador final.
* **Padrão de Repositório:** Iniciado o isolamento de dados com `json_repo.py`. A interface (ABC) será adicionada a seguir para permitir a futura transição de JSON para base de dados (ex: SQLAlchemy/Redis) sem necessidade de alterar as regras de negócio no `TaskManager`.
* **Observabilidade:** O pacote nativo `logging` foi configurado para guardar registos locais (ficheiro `logs`). A adoção do Sentry está planeada como próximo passo para garantir monitorização e alertas.