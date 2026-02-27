import pytest
import calculator

def test_sumar():
    assert calculator.sumar(2, 3) == 5

def test_restar():
    assert calculator.restar(5, 2) == 3

def test_multiplicar():
    assert calculator.multiplicar(4, 3) == 12

def test_dividir():
    assert calculator.dividir(10, 2) == 5

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        calculator.dividir(10, 0)