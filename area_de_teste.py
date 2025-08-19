import os 
import copy

lista_geral_users = ['Gustavo', '10']
lista_a_recuperar_salva = ["", ""]

indices = range(len(lista_geral_users))
while True:
    print("\n", 20 * "-" + "Lista com índice" + 20 * "-")
    indices = range(len(lista_geral_users))
    for indice in indices:
        print(f'Valor {lista_geral_users[indice]} está no índice: {indice + 1}')
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão: \n").strip().lower()
    indice_externo = ''
    
    if entrada == "a":
        while True:
            try:
                indice_interno = int(input("Digite o índice desejado: "))
                if indice_interno <= len(lista_geral_users):
                    if indice_interno == "0":
                        nome_a_ser_alterado = input("Digite o nome desejado: ")
                        if len(nome_a_ser_alterado) >= 3:
                            lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_externo])
                            del lista_geral_users[indice_externo][indice_interno]
                            lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
                            print("Valor alterado com sucesso!")
                            break
                        else:
                            print("Erro: Nome deve possuir pelo menos 3 caracteres")
                    else:
                        quantidade_a_ser_alterada = int(input("Digite "))
                else:
                    print("Erro: Índice maior do que a lista, tente outro por favor!")
            except ValueError:
                print("Erro: Por favor digite um tipo correto!")
            except IndexError:
                print("Erro: Índice não existe na lista")
            except Exception:
                print("Erro: Erro Desconhecido")

            
    elif entrada == "r":
        print("")
    elif entrada == "n":
        print("")
    else:
        print("")