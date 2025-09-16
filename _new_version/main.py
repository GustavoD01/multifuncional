import os
from utilidades import *

def menu_principal():
    numero = False
    while numero == False:
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
            print("Valor inserido está incorreto/ em desacordo com o solicitado!")
    return a


def main():
    
    menu_principal()
    # criar_login()
    # realizar_login()
    # alterar_1_usuario()
    # alterar_2_usuarios()
    # cadastrar_1_usuario()
    # cadastrar_2_usuarios()
    # criar_usuarios()
    # finalizar_insercao_usuarios()
    # recuperar_1_usuario()
    # recuperar_2_usuarios()
    # contagem_regressiva()
    # curiosidades()
    # tela_inicial()
    # advinhe_o_numero()

if __name__ == "__main__":
    main()