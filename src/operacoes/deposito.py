from operacoes.transacao import Transacao 
from dominio.conta import Conta

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        #Executa e registra o depósito somente se bem-sucedido.
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)