import pytest
from dominio.cliente import PessoaFisica
from operacoes.contaCorrente import ContaCorrente

def criar():
    cliente = PessoaFisica("123", "Gabriel", "01-01-2000", "Rua X")
    conta = ContaCorrente(1, cliente, limite=500, limite_saques=3)
    return cliente, conta

def test_saque_excede_limite():
    cliente, conta = criar()

    resultado = conta.sacar(600)

    assert resultado is False
    assert conta.saldo == 0