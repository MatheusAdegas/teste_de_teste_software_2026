from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import *


def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == "14/12/2026" and cafe._codigo_barras == "1234567890" and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(NomeInvalidoError):
        Produto("", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)

def test_criar_produto_sem_preco():
    with pytest.raises(PrecoInvalidoError):
        Produto("cafe", None, 50, "14/12/2026", "1234567890", "alimenticio", 250)

def test_criar_produto_sem_estoque():
    with pytest.raises(EstoqueInvalidoError):
        Produto("cafe", 18, None, "14/12/2026", "1234567890", "alimenticio", 250)

def test_criar_produto_sem_validade():
    with pytest.raises(ValidadeInvalidaError):
        Produto("cafe", 18, 50, None, "1234567890", "alimenticio", 250)

def test_criar_produto_sem_barras():
    with pytest.raises(BarrasInvalidaError):
        Produto("cafe", 18, 50, "14/12/2026", None, "alimenticio", 250)

def test_criar_produto_sem_categoria():
    with pytest.raises(CategoriaInvalidaError):
        Produto("cafe", 18, 50, "14/12/2026", "1234567890", "", 250)

def test_criar_produto_sem_peso():
    with pytest.raises(PesoInvalidoError):
        Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", None)

def test_get_produto_nome():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.nome == "cafe"

def test_set_produto_nome():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.nome = "cafe"
    assert cafe.nome == "cafe"

def test_get_produto_preco():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.preco == 18

def test_set_produto_preco():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.preco = 18
    assert cafe.preco == 18

def test_get_produto_quant_estoque():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.quant_estoque == 50

def test_set_produto_quant_estoque():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.quant_estoque = 50
    assert cafe.quant_estoque == 50

def test_get_produto_validade():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.validade == "14/12/2026"

def test_set_produto_validade():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.validade = "14/12/2026"
    assert cafe.validade == "14/12/2026"

def test_get_produto_codigo_barras():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.codigo_barras == "1234567890"

def test_set_produto_codigo_barras():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.codigo_barras = "1234567890"
    assert cafe.codigo_barras == "1234567890"

def test_get_produto_categoria():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.categoria == "alimenticio"

def test_set_produto_categoria():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.categoria = "alimenticio"
    assert cafe.categoria == "alimenticio"

def test_get_produto_peso():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    assert cafe.peso == 250

def test_set_produto_peso():
    cafe = Produto("cafe", 18, 50, "14/12/2026", "1234567890", "alimenticio", 250)
    cafe.peso = 250
    assert cafe.peso == 250



