import os
#
#Essa nova implementação possuirá "crud" baseado em listas, simulando as opreações básicas. Como se trata de List in List, será necessário captação de 2 índices
#
lista_geral_users = [['GUSTAVO', '10'], ['ANA','2'],['ROBERTA','3']]
lista_recuperar = lista_geral_users

lista_a_recuperar_salva = []

while True:
    print("\n", 20 * "-" + "Lista com índices" + 20 * "-")
    indices = range(len(lista_geral_users))
    for indice in indices:
        print(f"Valor {lista_geral_users[indice]} está no índice: {indice + 1}")
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão:\n ").strip().lower()
    indice_externo = ""

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
                    print("ERRO: Índice maior do que a lista, tente outro por favor!")
            except ValueError:
                print("ERRO: Por favor digite um tipo correto")
            except IndexError:
                print("ERRO: Índice não existe na lista")
            except Exception:
                print("ERRO: Erro Desconhecido")
                
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
                        lista_a_recuperar_salva = lista_geral_users[indice_externo]
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
                        lista_a_recuperar_salva = lista_geral_users[indice_externo]
                        del lista_geral_users[indice_externo][indice_interno]
                        lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
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
                    nome_a_ser_alterado = input("Digite o nome desejado: ")
                    if len(nome_a_ser_alterado) >= 3:
                        lista_a_recuperar_salva.insert(indice_externo, lista_geral_users[indice_externo])
                        del lista_geral_users[indice_externo][indice_interno]
                        lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
                        print("Valor alterado com sucesso!")
                        indice_interno = 1
                        break
                    else:
                        print("Erro: Nome deve possuir pelo menos 3 caracteres!")
                while True:
                    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
                    if quantidade_a_ser_alterada.isdigit() == True:
                        del lista_geral_users[indice_externo][indice_interno]
                        lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
                        break
                    else:
                        print("Erro: Quantidade está incorreta!")
            else:
                print("Erro: Digite um valor válido!")
        #######################
        #Pede índice "interno"#
        #######################
    elif entrada == "r" and len(lista_a_recuperar_salva) >= 1:
        indice_interno = ''
        ##########################
        #Pedindo índice "externo"#
        ##########################
        while True:
            try:
                indice_externo = int(input("Digite o índice desejado: "))
                if indice_externo <= len(lista_geral_users):
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                    break
                else:
                    print("E")
        while indice_interno not in [0, 1]:
            deseja_alterar = input("Deseja alterar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
            if deseja_alterar == "n":
                indice_interno = 0
                lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                print("Valor foi alterado com sucesso!")
                indices = range(len(lista_a_recuperar_salva))
                for indice in indices:
                    print(f"Valor {lista_a_recuperar_salva[indice]} está no índice: {indice + 1}")
            elif deseja_alterar == "q":
                indice_interno = 1
                
            elif deseja_alterar == "t":
                indice_interno = 0
                
                indice_interno = 1 
                
            else:
                print("Erro: Digite um valor válido")
    elif entrada == "r" and len(lista_a_recuperar_salva) < 1:
        print("Erro: A lista está vazia, não é possível recuperar nada!")
    elif entrada == "n":
        break
    else:       
        print("Erro: Digite um valor válido")  



# while True:
#     entrada = input("\nDeseja alterar/recuperar algum item digitado? (Digite 'Recuperar' ou 'Alterar' ou 'Não' ): ").strip().lower()
    
                    
# #
# #Alteração 
# #
#     if entrada == "alterar":
#         while True:
#             valor_a_alterar = input("Digite o número do que deseja alterar? ('1' = Quantidade, '2' = Nome ou 'TODOS'): ").strip().lower()   
#             if valor_a_alterar == "1":
#                 valor_a_ser_inserido = input("Digite o valor desejado: ")
#                 while valor_a_ser_inserido.isdigit() == False:
#                     valor_a_ser_inserido = input("Digite novamente o valor desejado: ")
#                 else:
#                     valor_01 = lista_geral_users[0]
#                     lista_recuperar.append(valor_01)
#                     del lista_geral_users[0]
#                     lista_geral_users.insert(0, valor_a_ser_inserido)
#                     print("Valor alterado com sucesso!")
#                     lista_enumerada = enumerate(lista_geral_users)
#                     print(60 * "-")
#                     print(f"Situação atual da lista:  {next(lista_enumerada)} e {next(lista_enumerada)}")
#                     print(60 * "-")
#                     print("(*índice atual e item respectivamente)\n")
#                     print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                     break
#         #
# #Alteração nome
# #
#             elif valor_a_alterar == "2":
#                 valor_a_ser_inserido = input("Digite o nome desejado: ")
#                 while isinstance(valor_a_ser_inserido, str) == False:
#                     valor_a_ser_inserido = input("Digite novamente o nome desejado: ")
#                 else:
#                     valor_01 = lista_geral_users[1]
#                     lista_recuperar.append(valor_01)
#                     del lista_geral_users[1]
#                     lista_geral_users.insert(1, valor_a_ser_inserido)
#                     print("Nome alterado com sucesso!")
#                     # for indice, nome in enumerate(lista):
#                     #     print(nome, lista_geral_users[indice])
#                     lista_enumerada = enumerate(lista_geral_users)
#                     print(60 * "-")
#                     print(f"Situação atual da lista:  {next(lista_enumerada)} e {next(lista_enumerada)}")
#                     print(60 * "-")
#                     print("(*índice atual e item respectivamente)\n")
#                     print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                     break
        
#             elif valor_a_alterar == 'todos':
#                 valor_a_ser_inserido = input("Digite a quantidade desejada: ")
#                 valor_01 = lista_geral_users[0]
#                 lista_recuperar.append(valor_01)
#                 del lista_geral_users[0]
#                 lista_geral_users.insert(0, valor_a_ser_inserido)
#                 valor_a_ser_inserido = input("Digite o nome desejado: ")
#                 valor_01 = lista_geral_users[1]
#                 lista_recuperar.append(valor_01)
#                 del lista_geral_users[1]
#                 lista_geral_users.insert(1, valor_a_ser_inserido)
#                 print("Valores alterados com sucesso!")
#                 print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                 break
#             else:
#                 continue
# #
# #Recuperar número
# #
#     elif entrada == 'recuperar':
#         if lista_recuperar == []:
#             print("Você não tem valores a recuperar, insira uma opção válida")
#         else:
#             while True:
#                 try:
#                     valor_a_recuperar = input("Digite o que deseja recuperar ('1' - Quantidade, '2' - Nome ou 'TODOS'): ").strip().lower()

#                     if valor_a_recuperar == '1':
#                         lista_geral_users[0] = lista_recuperar[0]
#                         print("Quantidade recuperado com sucesso!")
#                         print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                         break
#                     elif valor_a_recuperar == '2':
#                         lista_geral_users[1] = lista_recuperar[1]
#                         print("Nome recuperado com sucesso!")
#                         print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                         break
#                     elif valor_a_recuperar == 'todos':
#                         lista_geral_users = lista_recuperar.copy()
#                         print("Dados recuperados com sucesso!")
#                         print("Nome: ", lista_geral_users[1], ", quantidade de água ingerida: ", lista_geral_users[0])
#                         break
#                 except ValueError:
#                     print("Por favor digite um tipo correto")
#                 except IndexError:
#                     print("Índice não existe na lista")
#                 except Exception:
#                     print("Erro Desconhecido")
# #
# #Nada a alterar 'Não'
# #
#     elif entrada in ["não", "nao"]:
#         break
#     #