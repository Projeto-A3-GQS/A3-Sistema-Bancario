from typing import List

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
        return list(self._contas)

    def adicionar_conta(self, conta: "Conta") -> None:
        self._contas.append(conta)

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao") -> None:
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
