
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