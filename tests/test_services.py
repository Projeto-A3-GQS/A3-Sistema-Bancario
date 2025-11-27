from unittest.mock import patch
from app.services import buscar_cliente_por_cpf, criar_cliente
from dominio.cliente import PessoaFisica

def test_buscar_cliente_encontra():
    clientes = [
        PessoaFisica("111", "Gabriel", "01-01-2000", "Rua X")
    ]

    cliente = buscar_cliente_por_cpf("111", clientes)

    assert cliente is not None
    assert cliente.nome == "Gabriel"

@patch("builtins.input", side_effect=["111", "Gabriel", "01-01-2000", "Rua X"])
def test_criar_cliente(mock_input):
    clientes = []

    criar_cliente(clientes)

    assert len(clientes) == 1
    assert clientes[0].cpf == "111"
