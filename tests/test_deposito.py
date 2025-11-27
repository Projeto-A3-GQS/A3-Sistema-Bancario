from operacoes.deposito import Deposito
from dominio.cliente import PessoaFisica
from dominio.conta import Conta

def criar():
    cliente = PessoaFisica("123", "Gabriel", "01-01-2000", "Rua X")
    conta = Conta.nova_conta(cliente, 1)
    return cliente, conta

def test_registro_deposito_adiciona_historico():
    cliente, conta = criar()
    deposito = Deposito(200)

    deposito.registrar(conta)

    assert conta.saldo == 200
    assert len(conta.historico.transacoes) == 1
    assert conta.historico.transacoes[0]["tipo"] == "Deposito"
