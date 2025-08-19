import os 
import copy

lista_geral_users = ['Gustavo', '10']
lista_a_recuperar_salva = ["", ""]

indices = range(len(lista_geral_users))
while True:
    entrada = ''
    entrada_interna = ''
    indice_interno = ''
    print("\n", 20 * "-" + "Lista" + 20 * "-")
    print(f'Nome: {lista_geral_users[0]}')
    print(f'Quantidade de água ingerida/dia: {lista_geral_users[1]}L')
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão: \n").strip().lower()

    if entrada == "a":
        while True:
            # try:
                entrada_interna = input("Digite se você deseja alterar o [N]ome ou a [Q]uantidade: ").strip().lower()
                if entrada_interna == "n":
                    indice_interno = 0
                    nome_a_ser_alterado = input("Digite o nome desejado: ")
                    if len(nome_a_ser_alterado) >= 3:
                        lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
                        del lista_geral_users[indice_interno]
                        lista_geral_users.insert(indice_interno, nome_a_ser_alterado)
                        print("Nome alterado com sucesso!")
                        break
                    else:
                        print("Erro: O nome deve possuir pelo menos 3 caracteres!")
                elif entrada_interna == "q":
                    indice_interno = 1
                    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
                    if quantidade_a_ser_alterada.isdigit() == True:
                        lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
                        del lista_geral_users[indice_interno]
                        lista_geral_users.insert(indice_interno, quantidade_a_ser_alterada)
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
            
    elif entrada == "r":
        entrada_interna = input("Digite se você deseja recupera  o [N]ome ou a [Q]uantidade: ").strip().lower()
        if entrada_interna == 'n':
            indice_interno = 0
            if lista_geral_users[indice_interno] == lista_a_recuperar_salva[indice_interno]:
                lista_geral_users[indice_interno] = lista_a_recuperar_salva[indice_interno]
                print("Nome foi recuperado com sucesso!")
                break
        elif entrada_interna == 'q':
            indice_interno = 1
        else:
            print("Erro: Digite uma opção válida!")
    elif entrada == "n":
        print("")
    else:
        print("")