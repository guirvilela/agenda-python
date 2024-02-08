from visualizar_contato import retorna_contatos


def marcar_favorito(contatos):
    print("\n3. Editar contato")

    retorna_contatos(contatos)

    usuario_selecionado = int(
        input("\nDigite o número do contato que deseja favoritar: ")
    )

    usuario_tratado = usuario_selecionado - 1

    contato_encontrado = contatos[usuario_tratado]

    if (
        contato_encontrado["favorito"]
        and usuario_tratado >= 0
        and usuario_tratado < len(contatos)
    ):
        contato_encontrado["favorito"] = False

        print(f"\nContato {usuario_selecionado} marcado como favorito ")

        print(
            f"""\n{usuario_selecionado}. "[]" nome: {contato_encontrado['nome']}
      telefone: {contato_encontrado['telefone']}
      email: {contato_encontrado['email']}"""
        )

    elif not contato_encontrado["favorito"]:
        contato_encontrado["favorito"] = True

        print(f"\nContato {usuario_selecionado} marcado como favorito ")

        print(
            f"""\n{usuario_selecionado}. "[☆]" nome: {contato_encontrado['nome']}
      telefone: {contato_encontrado['telefone']}
      email: {contato_encontrado['email']}"""
        )
    else:
        print("Nenhum contato encontrado")
