from __future__ import annotations
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from typing import List


class RegraDeNegocioError(Exception):
    """Erro lançado quando uma operação viola uma regra de negócio."""
    pass



class Cliente:
    #Representa um cliente do banco.
    def __init__(self, endereco: str) -> None:
        self._endereco: str = endereco
        self._contas: List["Conta"] = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> List["Conta"]:
        # sempre retorna cópia para evitar alterações
        return list(self._contas)

    def adicionar_conta(self, conta: "Conta") -> None:
        #Associa uma conta ao cliente.
        self._contas.append(conta)

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao") -> None:
        #Executa uma transação na conta informada.
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, endereco: str) -> None:
        super().__init__(endereco)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: str = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento


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


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        nro_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = nro_saques >= self._limite_saques

        if excedeu_limite:
            print("\nO valor do saque excede o limite, a operação falhou!!!")

        elif excedeu_saques:
            print("\nNúmero máximo de saques excedido, a operação falhou!!!")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    @property
    def transacoes(self):
        return self._transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        transacao_efetuada = conta.sacar(self.valor)

        if transacao_efetuada:
            conta.historico.adicionar_transacao(self)

    @property
    def valor(self):
        return self._valor


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        transacao_efetuada = conta.depositar(self.valor)

        if transacao_efetuada:
            conta.historico.adicionar_transacao(self)

    @property
    def valor(self):
        return self._valor


def menu_acesso():
    menu_acesso = """\n
    ================ MENU ================
    [1]\tSacar
    [2]\tDepositar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta corrente
    [6]\tExibir contas
    [0]\tSair
    """
    return input(textwrap.dedent(menu_acesso))


def filtrar_cliente(cpf, clientes):
    filtrados = [c for c in clientes if c.cpf == cpf]
    return filtrados[0] if filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!!!")
        return
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacoes = conta.historico.transacoes
    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for t in transacoes:
            extrato += f"\n{t['tipo']}:\n\tR$ {t['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

    print("\nCliente criado com sucesso!!!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo encerrado!!!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\nConta criada com sucesso!!!")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        operacao = menu_acesso()

        if operacao == "1":
            sacar(clientes)

        elif operacao == "2":
            depositar(clientes)

        elif operacao == "3":
            exibir_extrato(clientes)

        elif operacao == "4":
            criar_cliente(clientes)

        elif operacao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif operacao == "6":
            listar_contas(contas)

        elif operacao == "0":
            break

        else:
            print("\nOperação inválida!!!")


main()
