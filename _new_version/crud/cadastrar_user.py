def cadastrar_1_usuario():
    lista_geral_users = []
    while True:
    ###############
    #Inserção Nome#
    ###############
        var_1 = input(("Digite o nome do seu cliente: "))
        if len(var_1) >= 3:
            lista_geral_users.append(var_1)
            print("Cliente inserido com sucesso!")
            break
        else:
            print("Nome deve conter pelo menos 3 caracteres!")
        while True:
        #####################
        #Inserção Quantidade#
        #####################
            var_2 = input(("Digite o corte realizado pelo cliente: "))
            if var_2.isdigit() == True: 
                lista_geral_users.append(var_2)
                print("Corte inserido com sucesso!")
                print(lista_geral_users)
                break
            else:
                print("Quantidade inserida incorreta!")
                ################################
                #Inserção de 2 ou mais Usuários#
                ################################

#Adionar futuramente
        #####################
        #elif qtd_user == '2':
        #####################

def cadastrar_2_usuarios():
    lista_geral_users = []
    while True:
        ##################
        #Inserção 1° Nome#
        ##################
        var_recebe = input(("Digite o nome do seu cliente: "))
        if len(var_recebe) >= 3:
            var_1 = var_recebe
            print("Cliente inserido com sucesso!")
            break
        else:
            print("Nome inserido deve conter pelo menos 3 caracteres!")
    while True:
        ########################
        #Inserção 1° Quantidade#
        ########################
        var_recebe = input(("Digite a quantidade de água ingerida pelo primeiro usuário : "))
        if var_recebe.isdigit() == True:
            var_2 = var_recebe
            print("Quantidade inserida com sucesso!")
            break
        else:
            print("Quantidade inserida está incorreta!")
            #################
            #Adição na Lista#
            #################
            lista_insercao_users = [var_1, var_2]
            lista_geral_users.append(lista_insercao_users)
            print(lista_geral_users)
            #############################
            #Inserção do segundo usuário#
            #############################
    while True:
        ##################
        #Inserção 2° Nome#
        ##################
        var_recebe = input(("Digite o nome do segundo usuário: "))
        if len(var_recebe) >= 3:
            var_1 = var_recebe
            print("Nome inserido com sucesso!")
            break
        else:
            print("Nome deve conter pelo menos 3 caracteres!")
    while True:
        ########################
        #Inserção 2° Quantidade#
        ########################
        var_recebe = input(("Digite a quantidade de água ingerida pelo segundo usuário: "))
        if var_recebe.isdigit() == True:
            var_2 = var_recebe
            print("Quantidade inserida com sucesso!")
            break
        else:
            print("Quantidade inserida está incorreta!")
            #################   
            #Adição na Lista#
            #################
            lista_insercao_users = [var_1, var_2]
            lista_geral_users.append(lista_insercao_users)
            print(lista_geral_users)
            #########################
            #Adicionar mais usuários#
            #########################
    while True:
        limpa_tela()
        print(lista_geral_users)
        continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
        if continuar == 's':
            while True:
                ####################
                #Inserção novo Nome#
                ####################
                var_recebe = input(("Digite o nome do novo usuário: "))
                if len(var_recebe) >= 3:
                    var_1 = var_recebe
                    print("Nome inserido com sucesso!")
                    break
                else:
                    print("Nome inserido está incorreto!")
        while True:
            ##########################
            #Inserção nova Quantidade#
            ##########################
            var_recebe = input(("Digite a quantidade de água ingerida pelo novo usuário: "))
            if var_recebe.isdigit() == True:
                var_2 = var_recebe
                print("Quantidade inserida com sucesso!")
                break
            else:
                print("Quantidade inserida está incorreta!")
                ###################
                #Adicição na Lista#
                ###################
                lista_insercao_users = [var_1, var_2]
                lista_geral_users.append(lista_insercao_users)
    else:
        print("Valor inválido, Tente Novamente!")
        ####################
        #Finalizar Inserção#
        ####################

    #Adicionar depois
    # elif continuar == 'n' and len(lista_geral_users) > 0:
    #     break