from transacao import Transacao 
from dominio.conta import Conta

class Saque(Transacao):
    def __init__(self, valor:float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        #Executa e registra o saque somente se bem-sucedido.
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)