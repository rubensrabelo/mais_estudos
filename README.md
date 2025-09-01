# Projeto


## Estrutura das pastas

```bash
src/
├── main.py
├── api/
│   ├── api_router.py                # centraliza os routers
│   ├── config/                      # novo pacote para configs globais
│   │   ├── __init__.py
│   │   └── plot_config.py           # matplotlib + seaborn configurados
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── movie_repository.py
│   │   └── preprocessing/
│   │       ├── __init__.py
│   │       ├── load_and_clean_dataset.py
│   │       └── feature_engineering.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── movies_hypotheses_router.py
│   │   ├── movies_info_router.py
│   │   ├── movies_plot_router.py
│   │   ├── movies_recommendation_router.py
│   │   └── movies_gross_analysis_router.py
│   │   ├── movies_overview_router.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── movies_hypotheses_service.py
│   │   ├── movies_info_service.py
│   │   ├── movies_plot_service.py
│   │   ├── movies_recommendation_service.py
│   │   ├── movies_gross_analysis_service.py
│   │   └── movies_overview_service.py.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── correlations.py
│   │   ├── summary_stats.py
│   │   ├── add_global_ranking.py
│   │   └── init_predict_genre.py.py
```