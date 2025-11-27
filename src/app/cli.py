from app.services import buscar_cliente_por_cpf, menu_acesso, selecionar_conta_cliente, criar_cliente, criar_conta, listar_contas
from operacoes.deposito import Deposito
from operacoes.saque import Saque
#Refatorar operações e depois alterar o menu de acordo
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = selecionar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = selecionar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!!!")
        return

    conta = selecionar_conta_cliente(cliente)
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
