# Adicionar um contato


def adicionar_contato(contatos: []):
    print("\n1. Adicionar um novo contato")

    nome = input("\nDigite o nome do seu contato: ")
    telefone = int(input("\nDigite o telefone do seu contato: "))
    email = input("\nDigite o email do seu contato: ")
    favorito = False

    contatos.append(
        {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    )

    print(f"\n{nome} adicionado com sucesso!")
    print("\n-----------------------------")
