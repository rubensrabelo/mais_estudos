## Estrutura do Projeto

```bash
frontend/
├── index.html            # página inicial com resumo
├── pages/
│   └── analysis.html     # página detalhada das análises (gráficos, hipóteses, etc.)
│   └── predict.html      # página para testar a previsão de IMDB
├── css/
│   └── style.css         # estilos globais
│   └── components.css
│   └── layout.css
│   └── typography.css
└── js/
    ├── analysis.js       # busca gráficos/insights da API e mostra
    └── predict.js        # formulário de input e request para API
```