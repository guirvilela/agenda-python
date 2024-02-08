# Visualizar contatos


def visualizar_contatos(contatos: []):
    print("\n2. Visualizar contatos")

    retorna_contatos(contatos)
    print("--------------------")


def retorna_contatos(contatos: []):
    for index, contato in enumerate(contatos):
        index_tratado = index + 1
        contato_favorito = "[☆]" if contato["favorito"] else "[]"

        print(
            f"""\n{index_tratado}. {contato_favorito} nome: {contato['nome']}
      telefone: {contato['telefone']}
      email: {contato['email']}"""
        )
