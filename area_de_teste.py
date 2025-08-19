lista_geral_users = ["Gustavo", "10"]

print(20 * "-", "Lista de Usuário(os)", 20 * "-", "\n")
indice_externo = range(len(lista_geral_users))
for indice_externo_2 in indice_externo:
        if indice_externo_2 == 0:
            print(f"{lista_geral_users[indice_externo_2]} ", end="")
        else:
            print(f"ingeriu {lista_geral_users[indice_externo_2]}L de água num dia e {int(lista_geral_users[indice_externo_2])/24:.2f}ml de água por hora!")
            print(f"Curiosidade, em hexadecimal você ingeriu {int(lista_geral_users[indice_externo_2]):08X}")
