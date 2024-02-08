# ✓ 0.  Lista de opções do que é possível de fazer

# ✓ 1. Adicionar Contato, Nome, Telefone, Email, Favorito

# ✓ 2.  Visualizar lista de contatos

# ✓ 3. Editar um contato

# ✓ 4. Marcar/Desmarcar como favorito

# ✓ 5. Ver lista de contatos favoritos

# ✓ 6. Apagar contato

from opcoes import lista_de_opcoes
from adicionar_contato import adicionar_contato
from visualizar_contato import visualizar_contatos
from editar_contato import editar_contato
from marcar_favorito import marcar_favorito
from apagar_contato import apagar_contato
from ver_lista_favoritos import ver_lista_favoritos

contatos = []

while True:
    lista_de_opcoes()

    opcao_digitada = int(input("\nDigite o número da opção desejada: "))

    if opcao_digitada == 1:
        adicionar_contato(contatos)
    elif opcao_digitada == 2:
        visualizar_contatos(contatos)
    elif opcao_digitada == 3:
        editar_contato(contatos)
    elif opcao_digitada == 4:
        marcar_favorito(contatos)
    elif opcao_digitada == 5:
        ver_lista_favoritos(contatos)
    elif opcao_digitada == 6:
        apagar_contato(contatos)
    else:
        print("\nAgenda finalizada")
        break
