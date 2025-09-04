from main import *

lista_geral_users = ["","",""]

def menu_principal():
    print(40 * "-","\n")
    print("Bem vindo ao sistema de cabeleireiro✂️\n")
    print(f"Sua lista atualmente {'lista'}\n")
    print(20 * " ↓")
    print("\nDigite a opção desejada: \n")
    print("[C]adastrar cliente(s)")
    print("[A]lterar cliente(s)")
    print("[D]eletar cliente(s)")
    print("[R]ecuperar cliente(s)\n")     
    print(20 * " ↑")
    valor_escolhido_menu = input("\n")

def analisa_valor_escolhido_menu(valor_escolhido_menu):
    if valor_escolhido_menu == "C":
        print()

menu_principal()