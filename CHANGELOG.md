# 📝 Changelog

Todas as alterações notáveis a este projeto serão documentadas neste ficheiro.

O formato baseia-se no [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), 
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - Preparação para a v0.1.0

### Adicionado
- Estrutura inicial de pastas baseada em Clean Architecture.
- Modelagem da entidade `Task` com IDs únicos (UUID) e timestamps.
- Repositório base para gestão de ficheiros JSON.
- Inicialização do sistema de monitorização Sentry.
- Interface de linha de comando base via Click (comandos: add, update, delete, mark-in-progress, mark-done, list).