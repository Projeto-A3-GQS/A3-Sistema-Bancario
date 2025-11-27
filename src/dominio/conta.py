from dominio.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nSaldo insuficiente, a operação falhou!!!")

        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!!!")
            return True

        else:
            print("\nValor informado é inválido, a operação falhou!!!")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!!!")
        else:
            print("\nO valor informado é inválido, a operação falhou!!!")
            return False

        return True

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico