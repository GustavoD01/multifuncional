from utilidades import limpa_tela

def alterar_2_usuarios():
    ###############################
    #Verifica se entrada é ALTERAR#
    ###############################
    indice_interno = ""
    ##########################
    #Pedindo índice "externo"#
    ##########################
    while True:
        try:
            indice_externo = int(input("Digite o índice desejado: "))
            if indice_externo <= len(lista_geral_users) and indice_externo > 0:
                limpa_tela()
                break
            else:
                limpa_tela()
            print("Erro: Índice está fora de range, tente outro por favor!")
        except ValueError:
            print("Erro: Por favor digite um tipo correto")
        except IndexError:
            print("Erro: Índice não existe na lista")
        except Exception:
            print("Erro: Erro Desconhecido")

    indice_externo = (indice_externo - 1)
    print(f"Você selecionou '{lista_geral_users[indice_externo]}'")
    #######################
    #Pede índice "interno"#
    #######################
    while indice_interno not in [0, 1]:
    deseja_alterar = input("Deseja alterar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
    if deseja_alterar == "n":
    ##############
    #Alterar Nome#
    ##############
    indice_interno = 0
    while True:
    nome_a_ser_alterado = input("Digite o nome desejado: ")
    if len(nome_a_ser_alterado) >= 3:
    lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
    limpa_tela()
    print("Valor alterado com sucesso!")
    # lista_enumerada = enumerate(lista_geral_users)
    break
    else:
    print("Erro: Nome deve possuir pelo menos 3 caracteres!")

    elif deseja_alterar == "q":
    ####################
    #Alterar Quantidade#
    ####################
    indice_interno = 1
    while True:
    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
    if quantidade_a_ser_alterada.isdigit() == True: 
    lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
    limpa_tela()
    print("Valor alterado com sucesso!")
    # lista_enumerada = enumerate(lista_geral_users)
    break
    else:
    print("Erro: Quantidade está incorreta")
    elif deseja_alterar == "t":
    ###############
    #Alterar Todos#
    ###############
    indice_interno = 0
    while True:
    ##############
    #Alterar Nome#
    ##############
    nome_a_ser_alterado = input("Digite o nome desejado: ")
    if len(nome_a_ser_alterado) >= 3:
    lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
    limpa_tela()
    print("Valor alterado com sucesso!")
    indice_interno = 1
    break
    else:
    print("Erro: Nome deve possuir pelo menos 3 caracteres!")

    print(lista_geral_users)
    while True:
    ####################
    #Alterar Quantidade#
    ####################
    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
    if quantidade_a_ser_alterada.isdigit() == True:
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
    limpa_tela()
    print("Valor alterado com sucesso!")
    break
    else:
    print("Erro: Quantidade está incorreta!")
    #################################
    #Verifica se entrada é RECUPERAR#
    #################################

def alterar_1_usuario():
    if entrada == "a":
    while True:
    # try:
    entrada_interna = input("Digite se você deseja alterar o [N]ome ou a [Q]uantidade: ").strip().lower()
    if entrada_interna == "n":
    indice_interno = 0
    ##############
    #Alterar Nome#
    ##############
    nome_a_ser_alterado = input("Digite o nome desejado: ")
    if len(nome_a_ser_alterado) >= 3:
    lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
    del lista_geral_users[indice_interno]
    lista_geral_users.insert(indice_interno, nome_a_ser_alterado)
    limpa_tela()
    print("Nome alterado com sucesso!")
    break
    else:
    print("Erro: O nome deve possuir pelo menos 3 caracteres!")
    continue
    elif entrada_interna == "q":
    indice_interno = 1
    ####################
    #Alterar Quantidade#
    ####################
    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
    if quantidade_a_ser_alterada.isdigit() == True:
    lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
    del lista_geral_users[indice_interno]
    lista_geral_users.insert(indice_interno, quantidade_a_ser_alterada)
    limpa_tela()
    print("Quantidade alterada com sucesso!")
    break
    else:
    print("Erro: A quantidade deve ser do tipo numérica!")
    continue
    else:
    print("Erro: Digite uma opção válida!")
    # except ValueError:
    #     print("Erro: Por favor digite um tipo correto!")
    # except IndexError:
    #     print("Erro: Índice não existe na lista")
    # except Exception:
    #     print("Erro: Erro Desconhecido")