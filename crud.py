# ====================> SUBALGORITMOS
import os


def cadastrar_contato(insta: str, d: dict, t: list) -> None:
    d['instagram'] = insta
    d['nome'] = input("Nome: ")
    d['idade'] = input("Idade: ")
    t.append(d.copy())


def consultar_contato(insta: str, t: list) -> int:  # insta = edson

    for i in range(len(t)):
        if insta == t[i]['instagram']:
            print("--------------------------------------")
            print(f"Instagram: {t[i]['instagram']}")
            print(f"Nome: {t[i]['nome']}")
            print(f"Idade: {t[i]['idade']}")
            print("--------------------------------------")
            return i
    return -1


def editar_contato(indice: int, t: list) -> None:
    t[indice]['instagram'] = input("Instagram: ")
    t[indice]['nome'] = input("Nome: ")
    t[indice]['idade'] = input("Idade: ")


def excluir_contato(indice: int, t: list) -> None:
    t[indice]['instagram'] = ""
    t[indice]['nome'] = ""
    t[indice]['idade'] = ""
    print("--------------------------------------")
    print("CONTATO EXCLUÍDO COM SUCESSO!")
    print("--------------------------------------")


# ====================> PRINCIPAL
# Estruturas
# Dicionario
contato = {
    'instagram': '',
    'nome': '',
    'idade': ''
}
# lista
contatos = list()
os.system("clear")

while True:
    print("""
        0 - SAIR
        1 - CADASTRAR
        2 - CONSULTAR
        3 - EDITAR
        4 - EXCLUIR
        """)
    opcao = int(input("Escolha: "))
    match opcao:
        case 0:
            break
        case 1:
            instagram = input("Instagram: ")
            if consultar_contato(instagram, contatos) == -1:
                cadastrar_contato(instagram, contato, contatos)
            else:
                print("--------------------------------------")
                print(f"O CONTATO '{instagram}' JÁ EXISTE!")
                print("--------------------------------------")

        case 2:
            instagram = input("Instagram: ")
            if consultar_contato(instagram, contatos) == -1:
                print("--------------------------------------")
                print("CONTATO NÃO EXISTE!")
                print("--------------------------------------")

        case 3:
            instagram = input("Instagram: ")
            ind = consultar_contato(instagram, contatos)
            if ind != -1:
                editar_contato(ind, contatos)
            else:
                print("--------------------------------------")
                print(f"O CONTATO '{instagram}' NÃO EXISTE!")
                print("--------------------------------------")
        case 4:
            instagram = input("Instagram: ")
            ind = consultar_contato(instagram, contatos)
            if ind != -1:
                excluir_contato(ind, contatos)
            else:
                print("--------------------------------------")
                print(f"O CONTATO '{instagram}' NÃO EXISTE!")
                print("--------------------------------------")


print(contatos)
