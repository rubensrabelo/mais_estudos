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
│   │       ├── clean_dataset.py
│   │       └── feature_engineering.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── movies_analysis_router.py
│   │   └── movies_info_router.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── movies_analysis_service.py
│   │   └── movies_info_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── correlations.py
│   │   └── summary_stats.py
```