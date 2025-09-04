# Desafio Cientista de Dados – Indicium / PProductions

## Descrição
Este projeto tem como objetivo explorar dados de filmes do IMDB, realizando **análises detalhadas**, **visualizações interativas** e o desenvolvimento de **modelos preditivos** para estimar a nota dos filmes.  

Além disso, o projeto inclui um **consumo de dados da API do IMDB**, permitindo atualizar métricas, manter o dataset atualizado e melhorar a acurácia do modelo preditivo ao longo do tempo.  
O principal desafio é lidar com dados incompletos e desbalanceados, especialmente para gêneros de filmes, garantindo que as análises e predições sejam consistentes e confiáveis.

## Demonstração do Projeto
Para entender melhor o funcionamento do projeto, assista aos vídeos demonstrativos disponíveis na pasta do Google Drive:

[Vídeos de Demonstração – Projeto IMDB](https://drive.google.com/drive/u/0/folders/18opVEXHO4GnHjTx6lHQfeWJ674sdIR-S)

## Estrutura do Projeto

```bash
frontend/
├── imdb_data_fetcher/      # Consome a API do IMDB e salva os dados em CSV
├── frontend/               # Interfaces web para visualização de análises, predições e métricas
├── files/                  # Contém o relatório em PDF e o arquivo .pkl do modelo preditivo
└── backend/                # API que processa CSV, gera gráficos, treina e expõe o modelo preditivo
```

## Mais informações

- Para detalhes sobre cada parte do projeto, consulte os READMEs específicos:

[Frontend](frontend/README.md)
[Backend](backend/README.md)

- Observações importantes:
    - A pasta files/ contém:
        - O relatório em PDF com os resultados do projeto
        - O arquivo .pkl com o modelo treinado para previsão da nota IMDB
- O código-fonte do modelo está localizado em backend/api/, organizado da seguinte forma:

```bash
backend/src/api/
├── utils/
│   └── preprocess_imdb.py              # Funções de pré-processamento dos dados do IMDB
├── services/
│   └── movies_imdb_rating_service.py   # Lógica de negócio para predição de notas
└── router/
    └── movies_imdb_rating_router.py    # Rotas da API para acesso ao modelo preditivo
```
