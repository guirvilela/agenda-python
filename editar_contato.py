from visualizar_contato import retorna_contatos


def editar_contato(
    contatos: [],
):
    print("\n3. Editar contato")

    retorna_contatos(contatos)

    usuario_selecionado = int(input("\nDigite o número do contato que deseja editar: "))

    usuario_tratado = usuario_selecionado - 1

    if usuario_tratado >= 0 and usuario_tratado < len(contatos):
        contato_encontrado = contatos[usuario_tratado]
        contato_favorito = "[☆]" if contato_encontrado["favorito"] else "[]"

        print(
            f"""\n{usuario_selecionado}. {contato_favorito} nome: {contato_encontrado['nome']}
      telefone: {contato_encontrado['telefone']}
      email: {contato_encontrado['email']}"""
        )

        print("\nDeixe os valores vazios que não precisam ser editados!")

        novo_nome = input("\nDigite o nome que deseja editar: ")
        novo_telefone = input("\nDigite o telefone que deseja editar: ")
        novo_email = input("\nDigite o email que deseja editar: ")

        contato_encontrado["nome"] = (
            contato_encontrado["nome"] if novo_nome == "" else novo_nome
        )
        contato_encontrado["telefone"] = (
            contato_encontrado["telefone"] if novo_telefone == "" else novo_telefone
        )
        contato_encontrado["email"] = (
            contato_encontrado["email"] if novo_email == "" else novo_email
        )

        print(f"\nContato {usuario_selecionado} editado com sucesso! ")

        print(
            f"""\n{usuario_selecionado}. {contato_favorito} nome: {contato_encontrado['nome']}
      telefone: {contato_encontrado['telefone']}
      email: {contato_encontrado['email']}"""
        )

        print("\n----------------------------")
    else:
        return print("\nNenhum usuário encontrado com esse id")
