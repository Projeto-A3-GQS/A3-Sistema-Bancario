import pytest
from src.dominio.conta import Conta
from src.dominio.cliente import PessoaFisica

def criar_cliente_e_conta():
    cliente = PessoaFisica("12345678900", "Gabriel", "01-01-2000", "Rua X")
    conta = Conta.nova_conta(cliente, 1)
    return cliente, conta

def test_deposito_valido():
    cliente, conta = criar_cliente_e_conta()

    resultado = conta.depositar(100)

    assert resultado is True
    assert conta.saldo == 100

def test_deposito_invalido():
    cliente, conta = criar_cliente_e_conta()

    resultado = conta.depositar(-50)

    assert resultado is False
    assert conta.saldo == 0

def test_saque_valido():
    cliente, conta = criar_cliente_e_conta()

    conta.depositar(200)
    resultado = conta.sacar(50)

    assert resultado is True
    assert conta.saldo == 150

def test_saque_acima_do_saldo():
    cliente, conta = criar_cliente_e_conta()

    conta.depositar(10)
    resultado = conta.sacar(100)

    assert resultado is False
    assert conta.saldo == 10
