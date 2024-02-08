from visualizar_contato import retorna_contatos


def apagar_contato(contatos: []):
    print("\n6. Apagar contato")

    retorna_contatos(contatos)

    usuario_selecionado = int(input("\nDigite o número do contato que deseja editar: "))

    usuario_tratado = usuario_selecionado - 1

    if usuario_tratado >= 0 and usuario_tratado < len(contatos):
        for index, contato in enumerate(contatos):

            if usuario_tratado == index:
                contatos.remove(contato)

                print("\nContato apagado com sucesso")
                print("\-----------------------------")
    else:
        print("\nContato não encontrado")
