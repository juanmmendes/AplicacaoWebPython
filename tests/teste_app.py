import pytest
from shiny.testing import TestServer
import pandas as pd
import sys
import os

# Adicionar o diretório raiz ao path para importar a aplicação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.app import app

def test_app_initialization():
    """Testa se a aplicação Shiny inicializa corretamente"""
    with TestServer(app) as server:
        assert server is not None

def test_slider_input():
    """Testa se o slider de número de observações funciona corretamente"""
    with TestServer(app) as server:
        # Valor padrão
        assert server.input.n == 20
        
        # Alterar o valor
        server.set_input("n", 50)
        assert server.input.n == 50

def test_tipo_grafico_input():
    """Testa se a seleção de tipo de gráfico funciona corretamente"""
    with TestServer(app) as server:
        # Valor padrão (primeiro item)
        assert server.input.tipo_grafico == "barras"
        
        # Alterar o valor
        server.set_input("tipo_grafico", "linha")
        assert server.input.tipo_grafico == "linha"

def test_dados_reactive():
    """Testa se os dados reativos são atualizados corretamente"""
    with TestServer(app) as server:
        # Definir o número de observações
        server.set_input("n", 10)
        
        # Acessar o DataFrame gerado
        result = server.get_value("tabela")
        
        # Verificar se tem o número correto de linhas
        assert len(result) == 10
        
        # Verificar se tem as colunas esperadas
        assert "x" in result.columns
        assert "y" in result.columns
        assert "grupo" in result.columns
        
        # Verificar os valores
        assert list(result["x"]) == list(range(1, 11))
        assert list(result["y"]) == list(range(10, 0, -1))