lista_geral_users = [["Gustavo", "10"], ["Ana", "3"]]

if isinstance(lista_geral_users[0], list):
                        indices = range(len(lista_geral_users))
                        for indice in indices:
                            for indicin in indice:
                                print(f"Valor {lista_geral_users[indice]} inserido com sucesso no índice: {indice}")
                        print(lista_geral_users)