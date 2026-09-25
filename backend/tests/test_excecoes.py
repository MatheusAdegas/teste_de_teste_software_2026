from backend.exceptions.excecoes import *

def test_exc_Nome():
    e = NomeInvalidoError("erro")
    assert e.__str__() == "erro"

def test_exc_Preco():
    e = PrecoInvalidoError("erro")
    assert e.__str__() == "erro"

def test_exc_Estoque():
    e = EstoqueInvalidoError("erro")
    assert e.__str__() == "erro"

def test_exc_Validade():
    e = ValidadeInvalidaError("erro")
    assert e.__str__() == "erro"

def test_exc_Barras():
    e = BarrasInvalidaError("erro")
    assert e.__str__() == "erro"

def test_exc_Categoria():
    e = CategoriaInvalidaError("erro")
    assert e.__str__() == "erro"

def test_exc_Peso():
    e = PesoInvalidoError("erro")
    assert e.__str__() == "erro"