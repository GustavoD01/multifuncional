import os
from utilidades import *

lista_geral_users = []

def menu_principal():
    while True:
        print("\nBem vindo ao HairGO✂️\n")
        print("[1] - Verificar lista clientes atual")
        print("[2] - Alterar cliente(s)")
        print("[3] - Deletar cliente(s)")
        print("[4] - Cadastrar cliente(s)")
        print("[5] - Recuperar cliente(s)")
        print("[6] - Encerrar programa")
        a = input()
        if a.isdigit() and int(a) in [1,2,3,4,5,6]:
            numero = True
            break
        else:
            limpa_tela()
            print("Valor inserido está incorreto / em desacordo com o solicitado!")
    return a

def apresenta_lista():
    limpa_tela()
    print(f"Seus clientes atuais são: {lista_geral_users}")

def cadastrar_cliente():
    print("\nCadastro de clientes ✂️\n")
    nome_1 = input("Digite o nome do cliente: ")
    corte_1 = input("Digite o corte desejado: ")
    lista_insercao_users = [nome_1, corte_1]
    lista_geral_users.append(lista_insercao_users)
    limpa_tela()
    print("Cliente adicionado com sucesso!")

def main():
    while True:
        opcoes = {
            "1": apresenta_lista,
            # "2": alterar_cliente,
            # "3": deletar_cliente,
            "4": cadastrar_cliente,
            # "5": recuperar_cliente,
            # "6": encerrar_programa
        }

        escolha = menu_principal()
        if escolha in opcoes and escolha != "6":
            opcoes[escolha]()
        elif escolha == "6":
            print("programa encerrado com sucesso!")
            break


if __name__ == "__main__":
    main()