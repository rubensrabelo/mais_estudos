# Desafio Cientista de Dados – Indicium / PProductions

## Descrição
Este projeto tem como objetivo explorar dados de filmes do IMDB, realizando **análises detalhadas**, **visualizações interativas** e o desenvolvimento de **modelos preditivos** para estimar a nota dos filmes.  

Além disso, o projeto inclui um **consumo de dados da API do IMDB**, permitindo atualizar métricas, manter o dataset atualizado e melhorar a acurácia do modelo preditivo ao longo do tempo.  
O principal desafio é lidar com dados incompletos e desbalanceados, especialmente para gêneros de filmes, garantindo que as análises e predições sejam consistentes e confiáveis.

## Estrutura do Projeto

```bash
frontend/
├── imdb_data_fetcher/      # Consome a API do IMDB e salva os dados em CSV
├── frontend/               # Interfaces web para visualização de análises, predições e métricas
└── backend/                # API que processa CSV, gera gráficos, treina e expõe o modelo preditivo
```

## Mais informações

Para detalhes sobre cada parte do projeto, consulte os READMEs específicos:

[Frontend](frontend/README.md)
[Backend](backend/README.md)
