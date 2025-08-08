lista_geral_users = []
while True:
    qtd_user = input(("Digite [I] para iniciar o programa, caso  [1] pessoa ou para [2] ou mais pessoas: "))
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
        var_1 = input(("Digite o nome do primeiro usuário: "))
        var_2 = input(("Digite a quanidade de água ingerida pelo primeiro usuário : "))
        lista_insercao_users = [var_1, var_2]
        lista_geral_users.append(lista_insercao_users)
        print(lista_geral_users)
    # Inserção dos segundo usuário 
        var_1 = input(("Digite o nome do segundo usuário: "))
        var_2 = input(("Digite a quantidade de água ingerida pelo segundo usuário: "))
        lista_insercao_users = [var_1, var_2]
        lista_geral_users.append(lista_insercao_users)
        print(lista_geral_users)
        while True:
            continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
            if continuar == 's':
                var_1 = input(("Digite o nome do novo usuário: "))
                var_2 = input(("Digite a quantidade de água ingerida pelo novo usuário: "))
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