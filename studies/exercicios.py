def par_ou_impar(arg):
    if arg % 2 == 0:
        print(f"Seu número {arg} é par")
    else:
        print(f"Seu número {arg} é ímpar")

entrada = par_ou_impar(int(input("Digite seu número: ")))
# ######################################
# #Expressõe Regulares (Lendário Regex)#
# ######################################
# import re
# import sys
# import random

# nove_digitos = ''
# # for _ in range(100) #loop para gerar 100 cpf
# for i in range(9):
#     nove_digitos += str(random.randint(0,9))

# print(nove_digitos)
# sys.exit()


# resposta = 's'
# while resposta == 's':
#     cpf = input("Digite seu CPF: ")

#     # nove_digitos = cpf[:9]

#     ##############
#     #Função do re#
#     ##############
#     cpf_enviado_usuario = re.sub(
#         #############################
#         #Seleciona apenas os números#
#         #############################
#         r'[^0-9]',
#             #####################
#             #Substitui por vazio#
#             #####################
#         '',     
#                 #############
#                 #Valor usado#
#                 #############
#         cpf     
#     )

#     print(f'Imprimindo CPF com regex: {cpf_enviado_usuario}')

#     ##########################################
#     #Retira os últimos 3 caracteres da string#
#     ##########################################
#     nove_digitos_cpf = cpf[:-3]
#     lista_cpf = []
#     contador = 10
#     soma_cpf_1 = 0
#     cpf_limpo = ""


#     ##########################
#     #Calcula 1° digito do CPF#
#     ##########################
#     for indice in cpf:
#         if indice.isdigit() == True and contador > 1:
#             cpf_limpo += indice
#             var = int(indice) * contador
#             contador = contador - 1
#             soma_cpf_1 += var

#     if (soma_cpf_1 * 10) % 11 > 9:
#         digito_1 = 0
#     else:    
#         digito_1 = (soma_cpf_1 * 10) % 11

#     cpf_limpo += str(digito_1)

#     ##########################
#     #Calcula 2° digito do CPF#
#     ##########################
#     contador = 11
#     soma_cpf_2 = 0
#     for indices in cpf_limpo:
#         if indices.isdigit() == True and contador > 1:
#             var = int(indices) * contador
#             contador = contador - 1
#             soma_cpf_2 += var

#     if (soma_cpf_2 * 10) % 11 > 9:
#         digito_2 = 0
#     else:    
#         digito_2 = (soma_cpf_2 * 10) % 11
    
#     ##########################
#     #Imprimindo CPF correto#
#     ##########################
#     print("O cpf correto seria: ", end="")
#     cpf_final = int(cpf_limpo[:-1])
#     cpf_formatado = f"{cpf_final:,}".replace(",",".")
#     print(cpf_formatado + "-" + str(digito_1) + str(digito_2))
#     print(f"CPF inserido: {cpf}")
    
#     resposta = input("Deseja verificar outro cpf? [S]im ou [N]ão: ")








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