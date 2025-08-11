lista_geral_users = []
while True:
    qtd_user = input(("Digite os seguintes caracteres para: [F]inalizar o programa , caso  [1] pessoa ou para [2] ou mais pessoas: "))
    if qtd_user == 'i':
        if len(lista_geral_users) <= 1:
            print("Lista está vazia, digite um ou mais usuários para iniciar o programa")
        else:
            print(lista_geral_users)
    elif qtd_user == '1':
        lista_geral_users = []
        while True:
            var_1 = input(("Digite seu nome: "))
            if len(var_1) >= 3:
                lista_geral_users.append(var_1)
                print("Nome inserido com sucesso!")
                break
            else:
                print("Valor incorreto para nome")
        while True:
            var_2 = input(("Digite quanto de água você ingeriu: "))
            if var_2.isdigit() == True: 
                lista_geral_users.append(var_2)
                print("Quantidade inserida com sucesso!")
                print(lista_geral_users)
                break
            else:
                print("Quantidade inserida incorreta!")
    elif qtd_user == '2':
        lista_geral_users = []
        while True:
            var_recebe = input(("Digite o nome do primeiro usuário: "))
            if len(var_recebe) >= 3:
                var_1 = var_recebe
                print("Nome inserido com sucesso!")
                break
            else:
                print("Nome inserido está incorreto!")
        while True:
            var_recebe = input(("Digite a quanidade de água ingerida pelo primeiro usuário : "))
            if var_recebe.isdigit() == True:
                var_2 = var_recebe
                print("Quantidade inserida com sucesso!")
                break
            else:
                print("Quantidade inserida está incorreta!")
            
        lista_insercao_users = [var_1, var_2]
        lista_geral_users.append(lista_insercao_users)
        print(lista_geral_users)
    # Inserção do segundo usuário 
        while True:
            var_recebe = input(("Digite o nome do segundo usuário: "))
            if len(var_1) >= 3:
                var_1 = var_recebe
                print("Nome inserido com sucesso!")
                break
            else:
                print("Nome inserido está incorreto!")
        while True:
            var_recebe = input(("Digite a quantidade de água ingerida pelo segundo usuário: "))
            if var_recebe.isdigit() == True:
                var_2 = var_recebe
                print("Quantidade inserida com sucesso!")
                break
            else:
                print("Quantidade inserida está incorreta!")
                
        lista_insercao_users = [var_1, var_2]
        lista_geral_users.append(lista_insercao_users)
        print(lista_geral_users)
        while True:
            continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
            if continuar == 's':
                while True:
                    var_recebe = input(("Digite o nome do novo usuário: "))
                    if len(var_1) >= 3:
                        var_1 = var_recebe
                        print("Nome inserido com sucesso!")
                        break
                    else:
                        print("Nome inserido está incorreto!")
                while True:
                    var_recebe = input(("Digite a quantidade de água ingerida pelo novo usuário: "))
                    if var_recebe.isdigit() == True:
                        var_2 = var_recebe
                        print("Quantidade inserida com sucesso!")
                        break
                    else:
                        print("Quantidade inserida está incorreta!")

                lista_insercao_users = [var_1, var_2]
                lista_geral_users.append(lista_insercao_users)
                print(lista_geral_users)
            elif continuar == 'n':
                break
            else:
                print("Valor inválido, Tente Novamente!")
    else:
        print("Valor inválido, Tente Novamente!")
        continue
                            #
                            #T.E.S.T.E
                            # lista_recebe_tudo = []

                            # var_recebe = input("Digite o 1° valor: ")
                            # var_01 = var_recebe
                            # print("Este é o var 01: ",var_01)
                            # var_recebe = input("Digite o 2° valor: ")
                            # var_02 = var_recebe
                            # print("Este é o var 02: ",var_02)

                            # lista_recebe = [var_01, var_02]
                            # print("Esta é a lista recebe: ",lista_recebe)
                            # lista_recebe_tudo.append(lista_recebe)
                            # print("Esta é a lista recebe tudo: ",lista_recebe_tudo)