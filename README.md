# Desafio MBA Engenharia de Software com IA - Full Cycle
Ingestão e Busca Semântica com LangChain e Postgres

## Configuração do ambiente:
1) Inicie seu python venv:

```python -m venv venv```

2) Instale as dependências do projeto:

```pip install -r requirements.txt```

3) Crie uma cópia do arquivo `.env.example` e renomeie para `.env`
4) Abra o arquivo `.env` e preencha as variáveis com os dados de seu ambiente
5) Suba o contâiner do banco de dados:

```docker compose up -d```

## Ingestão do PDF:
Para realizar a ingestão do arquivo PDF, execute:

```python src/ingest.py```

Após a ingestão, a aplicação estará pronta para uso.

### Executando a aplicação:
Para inicializar a aplicação, execute:

```python src/chat.py```