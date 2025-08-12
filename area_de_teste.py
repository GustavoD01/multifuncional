#
#Inserção código CRUD simples de lista
#
lista_geral_users = [['GUSTAVO', '10'], ['ANA','2'],['ROBERTA','3']]
lista_recuperar = lista_geral_users
permissao = False

indices = range(len(lista_geral_users))
for indice in indices:
                print(f"Valor {lista_geral_users[indice]} está no índice: {indice}")

seletor_lista = input("Digite o índice desejado: ")
seletor_lista = int(seletor_lista)

print(len(lista_geral_users))
print(lista_geral_users[seletor_lista])

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