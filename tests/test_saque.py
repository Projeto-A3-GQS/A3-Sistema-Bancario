from operacoes.saque import Saque
from dominio.cliente import PessoaFisica
from dominio.conta import Conta

def criar():
    cliente = PessoaFisica("123", "Gabriel", "01-01-2000", "Rua X")
    conta = Conta.nova_conta(cliente, 1)
    return cliente, conta

def test_registro_saque():
    cliente, conta = criar()
    conta.depositar(300)
    saque = Saque(100)

    saque.registrar(conta)

    assert conta.saldo == 200
    assert len(conta.historico.transacoes) == 1
    assert conta.historico.transacoes[0]["tipo"] == "Saque"
