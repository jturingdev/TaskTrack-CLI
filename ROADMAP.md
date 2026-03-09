# 🗺️ Roadmap Estratégico

## 🎯 Visão Geral
O Task Tracker evoluirá de um simples script CLI para uma aplicação robusta, incorporando base de dados relacional, cache em memória e exposição via API.

## 📦 Versão 0.1.0 - The Foundation (Atual)
- [ ] CLI estruturada com biblioteca **Click**.
- [ ] TUI (Terminal User Interface) básica com **Textual**.
- [ ] Observabilidade e rastreio de erros com **Sentry**.
- [ ] Persistência de dados local baseada em **JSON**.
- [ ] Arquitetura orientada a serviços (preparação para crescimento).

## 🗄️ Versão 0.2.0 - Persistence Layer Upgrade
- [ ] Implementação de **SQLAlchemy** (ORM).
- [ ] Migração do armazenamento JSON para **SQLite**.
- [ ] Padrão de injeção de dependência fortalecido.

## ⚡ Versão 0.3.0 - Performance & Caching
- [ ] Integração com **Redis**.
- [ ] Implementação de padrão arquitetural Medallion (Gateway -> Processor -> Orchestrator) focado no fluxo de dados.
- [ ] Lógica de invalidação de cache durante as operações CRUD.

## 🌐 Versão 0.4.0 - Web Exposure & Containerization
- [ ] Criação de uma Mini API assíncrona com **Starlette**.
- [ ] Documentação de endpoints.
- [ ] Empacotamento da aplicação com **Docker** (Dockerfile e `docker-compose.yml`).