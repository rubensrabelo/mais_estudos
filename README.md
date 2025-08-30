# Projeto


## Estrutura das pastas

```bash
src/
├── main.py
├── api/
│   ├── api_router.py                # centraliza os routers
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── movie_repository.py           # ponto de acesso ao dataset (get_dataset)
│   │   └── preprocessing/                # subpasta só para preparação do dataset
│   │       ├── __init__.py
│   │       ├── clean_dataset.py          # load_and_clean()
│   │       └── feature_engineering.py    # feature_engineering()
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