import sys
import os
import decimal
import copy

#import decimal
#
# Caso possuir algum número com ponto flutuante muito grande, é adequado utilizar esta função
# Exemplo: numero_2 = decimal.Decimal(0.7)
#

A = "ÁGUA" #Se variável for maiúscula, significa que é imutável
B = ''
print(B.zfill(100))
print(id(A)) #ID da variável A
frase_unida = '-'.join("abc")
print(frase_unida)
    #####################
    #Contagem regressiva#
    #####################
contador = 3
print(f'Iniciando programa em {contador}')
while contador > 0:
    contador -= 1
    if contador == 2:
        print("Não vou mostrar o 2")
        continue
    print(f'Iniciando programa em {contador}')

    #############
    #Boas-Vindas#
    #############
FRASE = "BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'%s💧 \n\n"% (A) #Variável string constante
frase_separada = FRASE.split(" ")
print(frase_separada)
print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
print(A[0])
print(A[-3])
print(A[2])
print(A[-1])

print("\n", A[::-1] ,"\n") #inverter string

    ##############
    #Jogo Números#
    ##############

print(20 * "-", "⚅ Advinhe o número ⚅", 20 * "-", "\n")

jogo = True
while jogo == True:
    jogar = input("Deseja jogar 'escolha um número?' ([S]im ou [N]ão): ").strip().lower()
    if jogar == "s":
        numero_correto = "4"
        for tentativa in range(5):
            numero_digitado = input("Escolha um número de 0 a 5: ").strip()
            if numero_digitado == numero_correto:
                print ("Acesso permitido")
                break
            else: 
                print(f'Acesso negado, tente novamente: {4 - tentativa} restantes')
        else:
            print("Esgotaram-se as tentativas, tente novamente.")
            sys.exit()
    elif jogar == 'n':
    ################
    #Início sistema#
    ################

        print("\n", 20 * "-", "Entrada no sistema", 20 * "-", "\n")
        user_senha_correta = False
        jogo = False
while True:
    entrada = input("Deseja entrar no sistema? ([S]im ou [N]ão): ").strip().lower() #startswith('s') -> retorna bool de acordo com inicio da palavra e tem o endswith que também retorna bool porém com fim da palavra
    if entrada == 's':
            #########################
            #Criação Usuário e Senha#
            #########################
            print("\n", 20 * "-", "Área de login", 20 * "-")
            print("\nCrie um Usuário e Senha")
            while user_senha_correta == False:
                usuario_permitido = input("Crie seu Usuário: ")
                if usuario_permitido == 's':
                    break
                else:    
                    senha_permitida = input("Crie sua senha: ")
                if len(usuario_permitido) < 3 and len(senha_permitida) < 3:
                    print("Digite um usuário ou senha com pelo menos 3 dígitos")
                else:
                    ############
                    #Área Login#
                    ############
                    print("ÁREA DE LOGIN:")
                        
                    while True:
                        #######################
                        #Login Usuário e Senha#
                        #######################
                        usuario = input("Digite seu Usuário: ")
                        senha = input("Digite sua senha: ")
                        if (usuario == usuario_permitido or usuario == "admin") and (
                        senha == senha_permitida):
                            # lista_nomes = 0
                            # string = 'b={nome2} a={nome1}'
                            # formato = string.format #quando uma função está dentro de um objeto é chamada de método
                            # nome1=A, nome2=lista_nomes #parâmetros
                            user_senha_correta = True
                            break
                        else:
                            print("Usuário ou senha incorreto! Tente novamente!")
                            continue
            #####################
            #Entrando no sistema#
            #####################
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
            print("\n", 20 * "-", "Seja bem vindo ao controle de água 💧", 20 * "-","\n")
            print("Curiosidade: a palavra", A,"é um(a)", type(A))
            #Caso a lista_nomes contivesse valores que nunca seriam alterados, seria desejável que criasse uma tupla
            #Formas de criar uma tupla:
            #lista_nomes = '1', 2, '3'
            #lista_nomes = ('1', 2, '3') -> uso de parênteses ao invés de
        ######################
        #Inserção de usuários#
        ######################
            lista_geral_users = []
            while True:
                qtd_user = input(("Digite os seguintes caracteres para:  Adicionar somente [1] pessoa ou para [2] ou mais pessoas ou [F]inalizar a inserção de usuários: ")).strip().lower()
                #######################
                #Inserção de 1 Usuário#
                #######################
                if qtd_user == '1':
                    lista_geral_users = []
                    while True:
                    ###############
                    #Inserção Nome#
                    ###############
                        var_1 = input(("Digite seu nome: "))
                        if len(var_1) >= 3:
                            lista_geral_users.append(var_1)
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Valor incorreto para nome")
                    while True:
                    #####################
                    #Inserção Quantidade#
                    #####################
                        var_2 = input(("Digite quanto de água foi ingerida: "))
                        if var_2.isdigit() == True: 
                            lista_geral_users.append(var_2)
                            print("Quantidade inserida com sucesso!")
                            print(lista_geral_users)
                            break
                        else:
                            print("Quantidade inserida incorreta!")
                ################################
                #Inserção de 2 ou mais Usuários#
                ################################
                elif qtd_user == '2':
                    lista_geral_users = []
                    while True:
                    ##################
                    #Inserção 1° Nome#
                    ##################
                        var_recebe = input(("Digite o nome do primeiro usuário: "))
                        if len(var_recebe) >= 3:
                            var_1 = var_recebe
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Nome inserido está incorreto!")
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
                    ###################
                    #Adicição na Lista#
                    ###################
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
                        if len(var_1) >= 3:
                            var_1 = var_recebe
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Nome inserido está incorreto!")
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
                    ###################
                    #Adicição na Lista#
                    ###################
                    lista_insercao_users = [var_1, var_2]
                    lista_geral_users.append(lista_insercao_users)
                    print(lista_geral_users)
                        #########################
                        #Adicionar mais usuários#
                        #########################
                    while True:
                        continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
                        if continuar == 's':
                            while True:
                            ####################
                            #Inserção novo Nome#
                            ####################
                                var_recebe = input(("Digite o nome do novo usuário: "))
                                if len(var_1) >= 3:
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
                            print(lista_geral_users)
                        elif continuar == 'n' and lista_geral_users > 0:
                            break
                        else:
                            print("Valor inválido, Tente Novamente!")
                ####################
                #Finalizar Inserção#
                ####################
                elif qtd_user == 'f':
                    if len(lista_geral_users) <= 1:
                        print("Lista está vazia, digite um ou mais usuários para iniciar o programa")
                    else:
                        print(lista_geral_users)
                        break
                else:
                    print("Valor inválido, Tente Novamente!")
                    continue

            ############################
            #Apresentar como Lista está#
            ############################
            indices = range(len(lista_geral_users))
            for indice in indices:
                print(f"Valor {lista_geral_users[indice]} inserido com sucesso no índice: {indice}")

#                  *****************************************************************************************************************************************************************
#                  *Essa nova implementação possuirá "crud" baseado em listas, simulando as opreações básicas. Como se trata de List in List, será necessário captação de 2 índices*
#                  *****************************************************************************************************************************************************************
#                  *Novo problema detectado, quando inserido apenas 1 pessoa, os índices internos acabam "virando" índices externos, solucionado da seguinte forma:*
#                  *************************************************************************************************************************************************

                ##############################################################
                #Verifica se os objetos dentro da Lista principal, são Listas#
                ##############################################################
                if isinstance(lista_geral_users[0], list):
                    lista_a_recuperar_salva = [["", ""] for _ in lista_geral_users]
                    #######################################
                    #Lista com Listas - 2 ou mais Usuários#
                    #######################################
                    while True:
                        print("\n", 20 * "-" + "Lista com índices" + 20 * "-")
                        indices = range(len(lista_geral_users))
                        for indice in indices:
                            print(f"Valor {lista_geral_users[indice]} está no índice: {indice + 1}")
                        ########
                        #Opções#
                        ########
                        entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão:\n ").strip().lower()
                        indice_externo = ""
                        
                        ###############################
                        #Verifica se entrada é ALTERAR#
                        ###############################
                        if entrada == "a":
                            indice_interno = ""
                            ##########################
                            #Pedindo índice "externo"#
                            ##########################
                            while True:
                                try:
                                    indice_externo = int(input("Digite o índice desejado: "))
                                    if indice_externo <= len(lista_geral_users):
                                        if os.name == 'nt':
                                            os.system('cls')  # Limpa tela no Windows
                                        else:
                                            os.system('clear')  # Limpa tela no Linux/Mac
                                        break
                                    else:
                                        print("Erro: Índice maior do que a lista, tente outro por favor!")
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
                                            print("Valor alterado com sucesso!")
                                            print(lista_a_recuperar_salva)
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
                                            break
                                        else:
                                            print("Erro: Quantidade está incorreta!")
                            else:
                                print("Erro: Digite um valor válido!")
                        #################################
                        #Verifica se entrada é RECUPERAR#
                        #################################
                        elif entrada == "r" and any(preenchida != ["", ""] for preenchida in lista_a_recuperar_salva):
                            indice_interno = ''
                            ##########################
                            #Pedindo índice "externo"#
                            ##########################
                            while True:
                                try:
                                    indice_externo = int(input("Digite o índice desejado: "))
                                    if indice_externo <= len(lista_geral_users):
                                        indice_externo = (indice_externo - 1)
                                        if os.name == "nt":
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        break
                                    else:
                                        print("E")
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
                                            if os.name == "nt":
                                                os.system('cls')
                                            else:
                                                os.system('clear')
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
                                            if os.name == "nt":
                                                os.system('cls')
                                            else:
                                                os.system('clear')
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
                                            print("Valor foi recuperado com sucesso!")
                                    #############################################################
                                    #Verifica se índice não está vazio ou quantidade não é igual#
                                    #############################################################
                                            indice_interno = 1
                                            if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
                                                lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                                                print("Valor recuperado com sucesso!")
                                                break
                                            else:
#                                               ?????????????????????????????????????????????????????
#                                               ?Repetição excessiva problema a ser resolvido no POO?
#                                               ?????????????????????????????????????????????????????
                                                if os.name == "nt":
                                                                os.system('cls')
                                                else:
                                                    os.system('clear')
                                                print("Erro: A quantidade é a mesma da atual!")
                                        else:
#                                            ?????????????????????????????????????????????????????
#                                            ?Repetição excessiva problema a ser resolvido no POO?
#                                            ?????????????????????????????????????????????????????
                                            if os.name == "nt":
                                                            os.system('cls')
                                            else:
                                                os.system('clear')
                                            print("Erro: O nome é o mesmo do atual")
                                    else:
#                                        ?????????????????????????????????????????????????????
#                                        ?Repetição excessiva problema a ser resolvido no POO?
#                                        ?????????????????????????????????????????????????????
                                        if os.name == "nt":
                                                        os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Erro: Digite um valor válido")
                            else:
                                print("Erro: Índice escolhido não possui quantidade e nome a recuperar!")
                        ################################
                        #Verifica se a Lista está vazia#
                        ################################
                        elif entrada == "r" and any(preenchida == ["", ""] for preenchida in lista_a_recuperar_salva):
                            if os.name == "nt":
                                            os.system('cls')
                            else:
                                os.system('clear')
                            print("Erro: A lista está vazia, não é possível recuperar nada!")
                        ###########################
                        #Verifica se entrada é NÃO#
                        ###########################
                        elif entrada == "n":
                            break
                        else:       
                            print("Erro: Digite um valor válido")
                else:
                    ############################################
                    #Fim Implementação Lista 2 ou mais Usuários#
                    ############################################

                    ################################
                    #Implementação da Lista "Única"#
                    ################################
                    lista_a_recuperar_salva = ["", ""]

                    indices = range(len(lista_geral_users))
                    while True:
                        entrada = ''
                        entrada_interna = ''
                        indice_interno = ''
                        print("\n", 20 * "-" + "Lista" + 20 * "-")
                        print(f'Nome: {lista_geral_users[0]}')
                        print(f'Quantidade de água ingerida/dia: {lista_geral_users[1]}L')
                        ########
                        #Opções#
                        ########
                        entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão: \n").strip().lower()
                            ###############################
                            #Verifica se entrada é ALTERAR#
                            ###############################
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
                                        if os.name == "nt":
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Nome alterado com sucesso!")
                                        break
                                    else:
                                        print("Erro: O nome deve possuir pelo menos 3 caracteres!")
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
                                        if os.name == "nt":
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Quantidade alterada com sucesso!")
                                        break
                                    else:
                                        print("Erro: A quantidade deve ser do tipo numérica!")
                                else:
                                    print("Erro: Digite uma opção válida!")
                            # except ValueError:
                            #     print("Erro: Por favor digite um tipo correto!")
                            # except IndexError:
                            #     print("Erro: Índice não existe na lista")
                            # except Exception:
                            #     print("Erro: Erro Desconhecido")

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
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    print("Nome foi recuperado com sucesso!")
                                else:
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
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
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    print("A quantidade foi alterada com sucesso!")
                                else:
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    print("Erro: A quantidade é a mesma da atual / ou não possui nome a ser recuperado!")
                            else:
                                print("Erro: Digite uma opção válida!")
                        ##########################################
                        #RECUPERAR selecionado, porém Lista vazia#
                        ##########################################
                        elif entrada == "r":
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print("Erro: Não existem valores a serem recuperados!")
                        ###################
                        #"NÃO" selecionado#
                        ###################
                        elif entrada == "n":
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print("Alterações Finalizadas!")
                            break
                        ################
                        #Opção inválida#
                        ################
                        else:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print("Digite uma opção válida!")

                    ###########################################################
                    #Após "NÃO" ser selecionado, apresenta dados sobre a Lista#
                    ###########################################################

                        #################################
                        #APRESENTA Lista vários Usuários#
                        #################################
                    if isinstance(lista_geral_users[0], list):
                        print(20 * "-", "Lista de Usuário(os)", 20 * "-", "\n")
                        indice_externo = range(len(lista_geral_users))
                        for indice_externo_2 in indice_externo:
                            indice_interno = range(len(lista_geral_users[indice_externo_2]))
                            for indice_interno_2 in indice_interno:
                                if indice_interno_2 == 0:
                                    print(f"{lista_geral_users[indice_externo_2][indice_interno_2]} ", end="")
                                else:
                                    print(f"ingeriu {lista_geral_users[indice_externo_2][indice_interno_2]}L de água num dia e {int(lista_geral_users[indice_externo_2][indice_interno_2])/24:.2f}!")
                                    print(f"Curiosidade, em hexadecimal você ingeriu {int(lista_geral_users[indice_externo_2][indice_interno_2]):08X}")

                        ###############################
                        #APRESENTA Lista Usuário Único#
                        ###############################
                    else:
                        print(20 * "-", "Lista de Usuário(os)", 20 * "-", "\n")
                        indice_externo = range(len(lista_geral_users))
                        for indice_externo_2 in indice_externo:
                            if indice_externo_2 == 0:
                                print(f"{lista_geral_users[indice_externo_2]} ", end="")
                            else:
                                print(f"ingeriu {lista_geral_users[indice_externo_2]}L de água num dia e {int(lista_geral_users[indice_externo_2])/24:.2f}ml de água por hora!")
                                print(f"Curiosidade, em hexadecimal você ingeriu {int(lista_geral_users[indice_externo_2]):08X}")
            else:
                print("Valor incorreto, Digite novamente!")
    ###################
    #"NÃO" selecionado#
    ###################
    elif entrada == 'n':
        print("Saindo do sistema...")#
        break
