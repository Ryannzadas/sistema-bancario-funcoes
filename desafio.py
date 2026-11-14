"""Sistema bancário com funções — desafio da formação Python da DIO.

Versão otimizada do sistema bancário: cada operação é uma função própria e
agora há cadastro de usuários (clientes) e de contas correntes.

Regras:
  - depositar(saldo, valor, extrato, /)            -> só argumentos posicionais
  - sacar(*, saldo, valor, extrato, limite, ...)   -> só argumentos nomeados
  - exibir_extrato(saldo, /, *, extrato)           -> posicional e nomeado
  - usuário: nome, data de nascimento, CPF (só números, sem repetir) e
    endereço no formato "logradouro, nº - bairro - cidade/UF";
  - conta: agência fixa "0001", número sequencial a partir de 1, ligada a
    um usuário existente; um usuário pode ter várias contas.
"""

import textwrap

AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.0


def menu():
    texto = """
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q]  Sair
    => """
    return input(textwrap.dedent(texto)).strip().lower()


def ler_valor(mensagem):
    """Pede um valor em reais. Aceita vírgula ou ponto; devolve None se for inválido."""
    texto = input(mensagem).strip().replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def so_digitos(texto):
    return "".join(ch for ch in texto if ch.isdigit())


# ---------------------------------------------------------------- operações


def depositar(saldo, valor, extrato, /):
    if valor is None or valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return saldo, extrato

    saldo += valor
    extrato.append(f"Depósito:\tR$ {valor:.2f}")
    print("\n=== Depósito realizado com sucesso! ===")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor is None or valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    elif valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
    else:
        saldo -= valor
        extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


# ------------------------------------------------------- usuários e contas


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = so_digitos(input("Informe o CPF (somente números): "))
    if len(cpf) != 11:
        print("\n@@@ CPF inválido! Ele precisa ter 11 dígitos. @@@")
        return

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ").strip()

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = so_digitos(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is None:
        print("\n@@@ Usuário não encontrado, criação de conta encerrada! @@@")
        return None

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 42)
        print(textwrap.dedent(linha))


# -------------------------------------------------------------------- main


def main():
    saldo = 0.0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = ler_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = ler_valor("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
