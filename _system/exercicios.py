cpf = "746.824.890-70"

#nove_digitos = cpf[:9]

lista_cpf = []
contador = 10
soma_cpf = 0

for indice in cpf:
    if indice.isdigit() == True and contador > 2:
        var = int(indice) * contador
        contador = contador - 1
        soma_cpf += var

if (soma_cpf * 10) % 11 > 9:
    digito_1 = 0
else:    
    digito_1 = (soma_cpf * 10) % 11

print(f"O primeiro digito é {digito_1}")

contador = 11
soma_cpf = 0
for indice in cpf:
    if indice.isdigit() == True and contador > 1:
        var = int(indice) * contador
        contador = contador - 1
        soma_cpf += var

if (soma_cpf * 10) % 11 > 9:
    digito_2 = 0
else:    
    digito_2 = (soma_cpf * 10) % 11

print(digito_2)









# Exercício realizado sem ajuda
# lista_compras = []

# while True:
#     print("Selecione uma opção")
#     opcao = input("[i]nserir [a]pagar [l]istar: ").strip().lower()
#     if opcao == 'i':
#         valor = input("Digite o item a adicionar no carrinho: ")
#         print(f'Valor: {valor}')
#         lista_compras.append(valor)
#     elif opcao == 'a':
#         for indice, nome in enumerate(lista_compras):
#             print(indice, lista_compras[indice])
#         idc = input("Digite o índice para apagar: ")
#         idc = int(idc)
#         valor_apagado = lista_compras[idc]
#         del lista_compras[idc]
#         print(f"Item apagado = {valor_apagado}")
#     elif opcao == 'l':
#         for indice, nome in enumerate(lista_compras):
#             print(indice, lista_compras[indice])
#     else:
#         print("Valor incorreto!")