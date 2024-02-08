def ver_lista_favoritos(contatos: []):
    print("\n5. Lista de favoritos")

    for index, contato in enumerate(contatos):
        index_tratado = index + 1

        contato_favorito = "[☆]" if contato["favorito"] else "[]"

        if contato["favorito"]:
            print(
                f"""\n{index_tratado}. {contato_favorito} nome: {contato['nome']}
      telefone: {contato['telefone']}
      email: {contato['email']}"""
            )
