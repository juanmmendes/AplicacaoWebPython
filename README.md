# Aplicação Web com Shiny para Python

Uma aplicação web interativa desenvolvida com Shiny para Python.

## Estrutura do Projeto

```
AplicacaoWebPython/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── components/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   ├── data/
│   └── static/
│       ├── css/
│       │   └── styles.css
│       ├── js/
│       └── images/
├── tests/
├── venv/
├── requirements.txt
├── README.md
└── .gitignore
```

## Requisitos

- Python 3.8+
- Shiny para Python
- Pandas
- NumPy
- Matplotlib
- Plotly

## Instalação

1. Clone o repositório:
```
git clone https://github.com/juanmmendes/AplicacaoWebPython.git
cd AplicacaoWebPython
```

2. Crie e ative um ambiente virtual:
```
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

## Execução

Para iniciar a aplicação:

```
shiny run app/app.py
```

Acesse a aplicação em `http://127.0.0.1:8000` no seu navegador.

## Funcionalidades

- Visualização de dados em diferentes tipos de gráficos
- Controles interativos para ajustar parâmetros
- Exibição de estatísticas
- Download de dados

## Desenvolvimento

Para adicionar novos componentes, crie módulos na pasta `app/components/`.
Para adicionar utilidades comuns, use a pasta `app/utils/`.

## Testes

Para executar os testes:

```
pytest
```