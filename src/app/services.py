import textwrap
from operacoes.deposito import Deposito
from operacoes.saque import Saque
from dominio.cliente import PessoaFisica
from operacoes.contaCorrente import ContaCorrente

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

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    if buscar_cliente_por_cpf(cpf, clientes):
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)

    print("\nCliente criado com sucesso!!!")

def criar_conta(numero_conta,clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!!!")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\nConta criada com sucesso!!!")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def buscar_cliente_por_cpf(cpf, clientes):
    cpf = cpf.strip()

    for cliente in clientes:
        if cliente.cpf.strip() == cpf:
            return cliente

    return None

def selecionar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!!!")
        return None

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]