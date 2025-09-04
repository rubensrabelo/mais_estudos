# Backend – Projeto IMDB

## Tecnologias Utilizadas
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Flask / FastAPI (ou framework usado)
- Joblib (para salvar modelos)
- Matplotlib / WordCloud (para visualizações)
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
4. Entre na pasta src:

```bash
cd src/
```

5. Execute o backend usando uvicorn:
```bash
uvicorn main:app
```
- `--reload` permite que o servidor recarregue automaticamente ao alterar o código.

6. Acessar a aplicação
O backend estará disponível para consumo pelo frontend e para execução de análises e predições, geralmente em http://127.0.0.1:8000/

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

- Os passos restantes são iguais 4 e 6 do tópico anterior

## Estrutura do Projeto

```bash
src/
├── main.py               # Arquivo principal para iniciar a aplicação
├── config/               # Configurações gerais do projeto
├── data/                 # CSVs e datasets utilizados
├── img/                  # Imagens geradas (gráficos, wordclouds)
├── api/
│   ├── repositories/     # Acesso e manipulação de dados
│   │   └── preprocessing/ # Funções de pré-processamento
│   ├── routes/           # Endpoints da API
│   ├── services/         # Lógica de negócio e processamento
│   └── utils/            # Funções utilitárias
```