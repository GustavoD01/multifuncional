def recuperar_2_usuarios():
    elif entrada == "r" and any(preenchida != ["", ""] for preenchida in lista_a_recuperar_salva):
    indice_interno = ''
    ##########################
    #Pedindo índice "externo"#
    ##########################
    while True:
    try:
    indice_externo = int(input("Digite o índice desejado: "))
    if indice_externo <= len(lista_geral_users) and indice_externo > 0:
    indice_externo = (indice_externo - 1)
    limpa_tela()
    break
    else:
    print("Erro: Índice está fora de range!")
    except ValueError:
    print("Erro: Por favor, digite um tipo correto!")
    except IndexError:
    print("Erro: Índice não existe na lista")
    except Exception:
    print("Erro: Erro Desconhecido")
    ###################################
    #Verifica se índice não está vazio#
    ###################################
    if len(lista_a_recuperar_salva[indice_externo][0]) >= 3 or lista_a_recuperar_salva[indice_externo][1].isdigit() == True:
    while indice_interno not in [0, 1]:
    deseja_alterar = input("Deseja recuperar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
    if deseja_alterar == "n":
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou nome não é igual#
    #######################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Valor foi recuperado com sucesso!")
    # indices = range(len(lista_a_recuperar_salva))
    # for indice in indices:
    #     print(f"Valor {lista_a_recuperar_salva[indice]} está no índice: {indice + 1}")
    break
    else:
    limpa_tela()
    print("Erro: O nome é o mesmo do atual!")
    elif deseja_alterar == "q":
    indice_interno = 1
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Valor foi recuperado com sucesso!")
    break
    else:
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual!")
    elif deseja_alterar == "t":  
    ###############
    #Alterar Todos#
    ############### 
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou nome não é igual#
    #######################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Nome recuperado com sucesso!")
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    indice_interno = 1
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Quantidade recuperada com sucesso!")
    break
    else:
    #                                               ?????????????????????????????????????????????????????
    #                                               ?Repetição excessiva problema a ser resolvido no POO?
    #                                               ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual!")
    else:
    #                                            ?????????????????????????????????????????????????????
    #                                            ?Repetição excessiva problema a ser resolvido no POO?
    #                                            ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: O nome é o mesmo do atual")
    else:
    #                                        ?????????????????????????????????????????????????????
    #                                        ?Repetição excessiva problema a ser resolvido no POO?
    #                                        ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: Digite um valor válido")
    else:
    print("Erro: Índice escolhido não possui quantidade e nome a recuperar!")
    ################################
    #Verifica se a Lista está vazia#
    ################################

def recuperar_1_usuario():
    #################################
    #Verifica se entrada é RECUPERAR#
    #################################
    elif entrada == "r" and lista_a_recuperar_salva != ["", ""]:
    #                           ***********************************************************
    #                           *FUTURA ATUALIZAÇÃO É SAIR DO LOOP, CASO ENTRAR SEM QUERER*
    #                           ***********************************************************
    entrada_interna = input("Digite se você deseja recupera  o [N]ome ou a [Q]uantidade: ").strip().lower()
    if entrada_interna == 'n':
    ################
    #Recuperar Nome#
    ################
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou Nome não é igual#
    #######################################################
    if lista_geral_users[indice_interno] != lista_a_recuperar_salva[indice_interno] and lista_a_recuperar_salva[indice_interno] != "":
    lista_geral_users[indice_interno] = lista_a_recuperar_salva[indice_interno]
    limpa_tela()
    print("Nome foi recuperado com sucesso!")
    else:
    limpa_tela()
    print("Erro: O nome é o mesmo do atual / ou não possui quantidade a ser recuperado!")
    elif entrada_interna == 'q':
    ######################
    #Recuperar Quantidade#
    ######################
    indice_interno = 1
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    if lista_geral_users[indice_interno] != lista_a_recuperar_salva[indice_interno] and lista_a_recuperar_salva[indice_interno] != "":
    lista_geral_users[indice_interno] = lista_a_recuperar_salva[indice_interno]
    limpa_tela()
    print("A quantidade foi alterada com sucesso!")
    else:
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual / ou não possui nome a ser recuperado!")
    else:
    print("Erro: Digite uma opção válida!")