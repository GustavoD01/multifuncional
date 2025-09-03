import os

from .utilidades import *
from .menus import *
from .crud import *
from .auth import *


def main():
    menu_opcoes()
    menu_principal()
    menu_lista_apresentacao()
    criar_login()
    realizar_login()
    alterar_1_usuario()
    alterar_2_usuarios()
    criar_1_usuario()
    criar_2_usuarios()
    criar_usuarios()
    finalizar_insercao_usuarios()
    recuperar_1_usuario()
    recuperar_2_usuarios()
    contagem_regressiva()
    curiosidades()
    tela_inicial()
    advinhe_o_numero()

if __name__ == "__main__":
    main()