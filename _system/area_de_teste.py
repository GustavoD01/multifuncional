lista_geral_users = [["Ana", 3], ["João", 7], ["Maria", 0], ["Pedro", 10], ["Lucas", 5], ["Carla", 2], ["Fernanda", 9], ["Bruno", 4], ["Paula", 8], ["Rafael", 6]]


print('Lista completa: ',*lista_geral_users)

print("* -> Desempacota e imprime sem colchetes")

nome = "Maria"
resultado = f"{nome} está na lista" if any(nome in sublista for sublista in lista_geral_users) else f"{nome} não está na lista"
print(resultado)
resultado = f'{nome} está na lista' if any(nome in sublista for sublista in lista_geral_users) else f'{nome} não está na lista'