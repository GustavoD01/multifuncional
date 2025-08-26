lista_geral_users = ["","",""]

def menu_principal():
    print("\n", 20 * "-", "Seja bem vindo ao controle para cabeleireiro ✂️", 20 * "-","\n")
    #Caso a lista_nomes contivesse valores que nunca seriam alterados, seria desejável que criasse uma tupla
    #Formas de criar uma tupla:
    #lista_nomes = '1', 2, '3'
    #lista_nomes = ('1', 2, '3') -> uso de parênteses ao invés de
    ######################
    #Inserção de usuários#
    ######################
#################################
#APRESENTA Lista vários Usuários#
#################################

def menu_lista_apresentacao():
    if isinstance(lista_geral_users[0], list) and "" not in lista_geral_users:
        print(20 * "-", "Lista de Usuário(os)", 20 * "-", "\n")
        indice_externo = range(len(lista_geral_users))
        for indice_externo_2 in indice_externo:
            indice_interno = range(len(lista_geral_users[indice_externo_2]))
        for indice_interno_2 in indice_interno:
            if indice_interno_2 == 0:
                print(f"{lista_geral_users[indice_externo_2][indice_interno_2]} ", end="")
        else:
            print(f"ingeriu {lista_geral_users[indice_externo_2][indice_interno_2]}L de água num dia e {int(lista_geral_users[indice_externo_2][indice_interno_2])/24:.2f}!")
            print(f"Curiosidade, em hexadecimal você ingeriu {int(lista_geral_users[indice_externo_2][indice_interno_2]):08X}L")
            print("\n", 20 * "-", "Entrada no sistema", 20 * "-", "\n")
        ###############################
        #APRESENTA Lista Usuário Único#
        ###############################
    elif isinstance(lista_geral_users[0], str) and "" not in lista_geral_users:
        print("\n", 20 * "-", "Lista do Usuário", 20 * "-", "\n")
        indice_externo = range(len(lista_geral_users))
        for indice_externo_2 in indice_externo:
            if indice_externo_2 == 0:
                print(f"{lista_geral_users[indice_externo_2]} ", end="")
        else:
            print(f"ingeriu {lista_geral_users[indice_externo_2]}L de água num dia e {int(lista_geral_users[indice_externo_2])/24:.2f}ml de água por hora!")
            print(f"Curiosidade, em hexadecimal você ingeriu {int(lista_geral_users[indice_externo_2]):08X}L")
            print('Lista completa: ',*lista_geral_users)
            Permissao = False
            print("\n", 20 * "-", "Entrada no sistema", 20 * "-", "\n")
    else: 
        print("A base de clientes está vazia! Adicione seu primeiro cliente!\n")

def menu_opcoes():
    entrada = input("Digite ")