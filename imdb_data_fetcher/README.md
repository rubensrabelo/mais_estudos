# Consumo da API do IMDB – Projeto IMDB

## Tecnologias Utilizadas
- Python 3.x
- Pandas
- Outras bibliotecas conforme `requirements.txt`

## Como Usar

### Utilizando o PIP

Para rodar a aplicação localmente, siga os passos abaixo:

1. Crie um ambiente virtual
rode o comando abaixo na pasta backend/:
```bash
python -m venv venv
```

2. Ativar o Ambiente Virtual
Ative o ambiente virtual para isolar as dependências do projeto. No terminal, execute o seguinte comando:

- Linux / MacOS
```bash
source venv/bin/activate
```

- Windows
```bash
venv\Scripts\activate
```

3. Instale as dependências listadas em `requirements.txt`:
```bash
pip install -r requirements.txt
```

4. Execute na pasta raiz:
```bash
python -m src.main
```

### Utilizando o UV

#### Descrição 
O `uv` é um gerenciador de pacotes moderno e super rápido para Python. Ele foi criado para ser uma alternativa ao pip, com foco em velocidade, segurança e simplicidade. Ele instala dependências de forma muito mais ágil, especialmente em projetos com muitos pacotes.

#### Como usar
Para rodar a aplicação localmente, siga os passos abaixo:

1. Instalar o uv
Antes de tudo, você precisa instalar o uv no seu ambiente Python. Execute:
```bash
pip install uv
```

2. Crie um ambiente virtual
rode o comando abaixo na pasta backend/:
```bash
uv venv
```

3. Ativar o Ambiente Virtual
Ative o ambiente virtual para isolar as dependências do projeto. No terminal, execute o seguinte comando:

- Linux / MacOS
```bash
source .venv/bin/activate
```

- Windows
```bash
.venv\Scripts\activate
```

4. Instale as dependências listadas em `requirements.txt`:
```bash
uv add pyproject.toml 
```

- Execute o passo 4 do tópico anterior

```bash
imdb_data_fetcher/
└── src/
    ├── main.py           # Arquivo principal para execução do script
    └── imdb/             # Pacote com módulos para manipulação e consumo da API do IMDB
```