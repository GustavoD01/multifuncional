
# # Refatorar código = editar seu código

# def perimetro():
#     print("Calcular perimetro de um quadrado ou retângulo")
#     a = int(input("Digite o lado A: "))
#     b = int(input("Digite o lado B: "))
#     # global b -> variável (O global deixa a variável interna do escopo da função "pública", ou seja, b poderia ser utilizado sem "chamar" função)
#     return a, b

# def vericador(a, b):
#     if a == b:
#         resultado = (a * 2) + (b * 2)
#         print(f'O seu quadrado tem um perimetro de {resultado}')
#     else:
#         resultado = (a * 2) + (b * 2)
#         print(f'O seu retângulo tem um perimetro de {resultado}')

# valores = perimetro()
# vericador(*valores)

#######################################################################################

# senha = aaa1321
# valida = True

# for i in range(len(senha) - 2):
#     if senha[i] == senha[i + 1] == senha[i + 2]:
#         valida = False
#         break

# if valida:
#     print("Senha válida")
# else:
#     print("Senha inválida, não pode conter repetição de caracteres!")




# print("\n", 20 * "-", "Área de login", 20 * "-")
# print("\nCrie um Usuário e Senha")
# while user_senha_correta == False:
#     while len(usuario_permitido) < 3 or len(senha_permitida) < 3:
#         usuario_permitido = input("Crie seu Usuário: ").strip().lower()
#         senha_permitida = input("Crie sua senha: ")
#         if usuario_permitido == 's':
#             user_senha_correta = True
#             break
#         elif 

#         elif len(usuario_permitido) >= 3 and len(senha_permitida) >= 3:
#             break
#         else:
#             print("Digite um usuário ou senha com pelo menos 3 dígitos")
#         ############
#         #Área Login#
#         ############

#     print("ÁREA DE LOGIN:")
#     while True and user_senha_correta == False:
#         #######################
#         #Login Usuário e Senha#
#         #######################
#         usuario = input("Digite seu Usuário: ").strip().lower()
#         senha = input("Digite sua senha: ")
#         if (usuario == usuario_permitido or usuario == "admin") and (
#         senha == senha_permitida):
#             # lista_nomes = 0
#             # string = 'b={nome2} a={nome1}'
#             # formato = string.format #quando uma função está dentro de um objeto é chamada de método
#             # nome1=A, nome2=lista_nomes #parâmetros
#             user_senha_correta = True
#             break
#         else:
#             print("Usuário ou senha incorreto! Tente novamente!")




# lista_geral_users = [["Ana", 3], ["João", 7], ["Maria", 0], ["Pedro", 10], ["Lucas", 5], ["Carla", 2], ["Fernanda", 9], ["Bruno", 4], ["Paula", 8], ["Rafael", 6]]


# print('Lista completa: ',*lista_geral_users)

# print("* -> Desempacota e imprime sem colchetes")

# nome = "Maria"
# resultado = f"{nome} está na lista" if any(nome in sublista for sublista in lista_geral_users) else f"{nome} não está na lista"
# print(resultado)
# resultado = f'{nome} está na lista' if any(nome in sublista for sublista in lista_geral_users) else f'{nome} não está na lista'