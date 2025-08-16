import sys
import os
import decimal

#import decimal
#
# Caso possuir algum número com ponto flutuante muito grande, é adequado utilizar esta função
# Exemplo: numero_2 = decimal.Decimal(0.7)
#

A = "ÁGUA" #Se variável for maiúscula, significa que é imutável
B = ''
print(B.zfill(100))
print(id(A)) #ID da variável A
frase_unida = '-'.join("abc")
print(frase_unida)

#Contagem regressiva
contador = 3
print(f'Iniciando programa em {contador}')
while contador > 0:
    contador -= 1
    if contador == 2:
        print("Não vou mostrar o 2")
        continue
    print(f'Iniciando programa em {contador}')

FRASE = "BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'%s💧 \n\n"% (A) #Variável string constante
frase_separada = FRASE.split(" ")
print(frase_separada)
print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
print(A[0])
print(A[-3])
print(A[2])
print(A[-1])

print("\n", A[::-1] ,"\n") #inverter string
#
#Advinhar número de 0 a 5
#
jogo = True
while jogo == True:
    jogar = input("Deseja jogar 'escolha um número?' (Sim ou Não): ").strip().lower()
    if jogar == "sim":
        numero_correto = "4"
        for tentativa in range(5):
            numero_digitado = input("Escolha um número de 0 a 5: ").strip()
            if numero_digitado == numero_correto:
                print ("Acesso permitido")
                break
            else: 
                print(f'Acesso negado, tente novamente: {4 - tentativa} restantes')
        else:
            print("Esgotaram-se as tentativas, tente novamente.")
            sys.exit()
    elif jogar in ["nao", "não"]:
#
#Acesso ao sistema
#
        jogo = False
while True:
    entrada = input("Deseja entrar no sistema? (Sim ou Não): ").strip().lower() #startswith('s') -> retorna bool de acordo com inicio da palavra e tem o endswith que também retorna bool porém com fim da palavra
    if entrada == 'sim':
            print("\nCrie um Usuário e Senha")
            while True:
                usuario_permitido = input("Crie seu Usuário: ")    
                senha_permitida = input("Crie sua senha: ")
                if len(usuario_permitido) < 3 and len(senha_permitida) < 3:
                    print("Digite um usuário ou senha com pelo menos 3 dígitos")
                else:
                    break
#
#Área Login
#
            print("ÁREA DE LOGIN:")
                
            while True:
                usuario = input("Digite seu Usuário: ")
                senha = input("Digite sua senha: ")
                if (usuario == usuario_permitido or usuario == "admin") and (
                senha == senha_permitida):
                    # lista_nomes = 0
                    # string = 'b={nome2} a={nome1}'
                    # formato = string.format #quando uma função está dentro de um objeto é chamada de método
                    # nome1=A, nome2=lista_nomes #parâmetros
                    break
                else:
                    print("Usuário ou senha incorreto! Tente novamente!")
                    continue
#
#Entrada sistema    
#
            print(50 * "_")
            print("\nSeja bem vindo ao controle de água 💧 \n")
            print("Curiosidade: a palavra", A,"é um(a)", type(A))
            #Caso a lista_nomes contivesse valores que nunca seriam alterados, seria desejável que criasse uma tupla
            #Formas de criar uma tupla:
            #lista_nomes = '1', 2, '3'
            #lista_nomes = ('1', 2, '3') -> uso de parênteses ao invés de
        #
        # NOVA INMPLENTAÇÃO
            lista_geral_users = []
            while True:
                qtd_user = input(("Digite os seguintes caracteres para:  Adicionar somente [1] pessoa ou para [2] ou mais pessoas ou [F]inalizar a inserção de usuários: ")).strip().lower()
                if qtd_user == '1':
                    lista_geral_users = []
                    while True:
                        var_1 = input(("Digite seu nome: "))
                        if len(var_1) >= 3:
                            lista_geral_users.append(var_1)
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Valor incorreto para nome")
                    while True:
                        var_2 = input(("Digite quanto de água você ingeriu: "))
                        if var_2.isdigit() == True: 
                            lista_geral_users.append(var_2)
                            print("Quantidade inserida com sucesso!")
                            print(lista_geral_users)
                            break
                        else:
                            print("Quantidade inserida incorreta!")
                elif qtd_user == '2':
                    lista_geral_users = []
                    while True:
                        var_recebe = input(("Digite o nome do primeiro usuário: "))
                        if len(var_recebe) >= 3:
                            var_1 = var_recebe
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Nome inserido está incorreto!")
                    while True:
                        var_recebe = input(("Digite a quanidade de água ingerida pelo primeiro usuário : "))
                        if var_recebe.isdigit() == True:
                            var_2 = var_recebe
                            print("Quantidade inserida com sucesso!")
                            break
                        else:
                            print("Quantidade inserida está incorreta!")
                        
                    lista_insercao_users = [var_1, var_2]
                    lista_geral_users.append(lista_insercao_users)
                    print(lista_geral_users)
                # Inserção do segundo usuário 
                    while True:
                        var_recebe = input(("Digite o nome do segundo usuário: "))
                        if len(var_1) >= 3:
                            var_1 = var_recebe
                            print("Nome inserido com sucesso!")
                            break
                        else:
                            print("Nome inserido está incorreto!")
                    while True:
                        var_recebe = input(("Digite a quantidade de água ingerida pelo segundo usuário: "))
                        if var_recebe.isdigit() == True:
                            var_2 = var_recebe
                            print("Quantidade inserida com sucesso!")
                            break
                        else:
                            print("Quantidade inserida está incorreta!")
                            
                    lista_insercao_users = [var_1, var_2]
                    lista_geral_users.append(lista_insercao_users)
                    print(lista_geral_users)
                    while True:
                        continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
                        if continuar == 's':
                            while True:
                                var_recebe = input(("Digite o nome do novo usuário: "))
                                if len(var_1) >= 3:
                                    var_1 = var_recebe
                                    print("Nome inserido com sucesso!")
                                    break
                                else:
                                    print("Nome inserido está incorreto!")
                            while True:
                                var_recebe = input(("Digite a quantidade de água ingerida pelo novo usuário: "))
                                if var_recebe.isdigit() == True:
                                    var_2 = var_recebe
                                    print("Quantidade inserida com sucesso!")
                                    break
                                else:
                                    print("Quantidade inserida está incorreta!")

                            lista_insercao_users = [var_1, var_2]
                            lista_geral_users.append(lista_insercao_users)
                            print(lista_geral_users)
                        elif continuar == 'n':
                            break
                        else:
                            print("Valor inválido, Tente Novamente!")
                elif qtd_user == 'f':
                    if len(lista_geral_users) <= 1:
                        print("Lista está vazia, digite um ou mais usuários para iniciar o programa")
                    else:
                        print(lista_geral_users)
                        break
                else:
                    print("Valor inválido, Tente Novamente!")
                    continue
        # FIM NOVA IMPLEMENTAÇÃO
        #
            indices = range(len(lista_geral_users))
            
            for indice in indices:
                print(f"Valor {lista_geral_users[indice]} inserido com sucesso no índice: {indice}")

#
#Inserção código CRUD simples de lista
#
            lista_recuperar = []
            permissao = False
            while permissao == False:
                entrada = input("Deseja alterar/recuperar algum item digitado? (Digite 'Recuperar' ou 'Alterar' ou 'Não' ): ").strip().lower()
                if entrada == "alterar":
                    
#
#Alteração 
#
                    while True:
                        valor_a_alterar = input("Digite o número do que deseja alterar? ('1' = Quantidade, '2' = Nome ou 'TODOS'): ").strip().lower()   
                        if valor_a_alterar == "1":
                            valor_a_ser_inserido = input("Digite o valor desejado: ")
                            while valor_a_ser_inserido.isdigit() == False:
                                valor_a_ser_inserido = input("Digite novamente o valor desejado: ")
                            else:
                                valor_01 = lista_nomes[0]
                                lista_recuperar.append(valor_01)
                                del lista_nomes[0]
                                lista_nomes.insert(0, valor_a_ser_inserido)
                                print("Valor alterado com sucesso!")
                                lista_enumerada = enumerate(lista_nomes)
                                print(60 * "-")
                                print(f"Situação atual da lista:  {next(lista_enumerada)} e {next(lista_enumerada)}")
                                print(60 * "-")
                                print("(*índice atual e item respectivamente)\n")
                                print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                break
#
#Alteração nome
#
                        elif valor_a_alterar == "2":
                            valor_a_ser_inserido = input("Digite o nome desejado: ")
                            while isinstance(valor_a_ser_inserido, str) == False:
                                valor_a_ser_inserido = input("Digite novamente o nome desejado: ")
                            else:
                                valor_01 = lista_nomes[1]
                                lista_recuperar.append(valor_01)
                                del lista_nomes[1]
                                lista_nomes.insert(1, valor_a_ser_inserido)
                                print("Nome alterado com sucesso!")
                                # for indice, nome in enumerate(lista):
                                #     print(nome, lista_nomes[indice])
                                lista_enumerada = enumerate(lista_nomes)
                                print(60 * "-")
                                print(f"Situação atual da lista:  {next(lista_enumerada)} e {next(lista_enumerada)}")
                                print(60 * "-")
                                print("(*índice atual e item respectivamente)\n")
                                print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                break
                        elif valor_a_alterar == 'todos':
                            valor_a_ser_inserido = input("Digite a quantidade desejada: ")
                            valor_01 = lista_nomes[0]
                            lista_recuperar.append(valor_01)
                            del lista_nomes[0]
                            lista_nomes.insert(0, valor_a_ser_inserido)
                            valor_a_ser_inserido = input("Digite o nome desejado: ")
                            valor_01 = lista_nomes[1]
                            lista_recuperar.append(valor_01)
                            del lista_nomes[1]
                            lista_nomes.insert(1, valor_a_ser_inserido)
                            print("Valores alterados com sucesso!")
                            print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                            break
                        else:
                            continue
#
#Recuperar número
#
                elif entrada == 'recuperar':
                    if lista_recuperar == []:
                        print("Você não tem valores a recuperar, insira uma opção válida")
                    else:
                        while True:
                            try:
                                valor_a_recuperar = input("Digite o que deseja recuperar ('1' - Quantidade, '2' - Nome ou 'TODOS'): ").strip().lower()

                                if valor_a_recuperar == '1':
                                    lista_nomes[0] = lista_recuperar[0]
                                    print("Quantidade recuperado com sucesso!")
                                    print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                    break
                                elif valor_a_recuperar == '2':
                                    lista_nomes[1] = lista_recuperar[1]
                                    print("Nome recuperado com sucesso!")
                                    print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                    break
                                elif valor_a_recuperar == 'todos':
                                    lista_nomes = lista_recuperar.copy()
                                    print("Dados recuperados com sucesso!")
                                    print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                    break
                            except ValueError:
                                print("Por favor digite um tipo correto")
                            except IndexError:
                                print("Índice não existe na lista")
                            except Exception:
                                print("Erro Desconhecido")
#
#Nada a alterar 'Não'
#
                elif entrada in ["não", "nao"]:
                    permissao = True
#
#Permissao True -> Resulta fim programa
#
                    print(lista_nomes)
                    agua = int(lista_nomes[0])
                    print("Parabéns ", lista_nomes[1], " sua quantidade de água foi alocada corretamente no sistema")
                    print("Parabéns, você bebeu ", agua , " litros de água até agora")
                    print("Em hexadecimal você bebeu", f'{agua:08X}')                        
                    print("Por hora você bebeu ", f'{agua/24:.2f}', " água")
                    _, nome, *_ = lista_nomes
                    print(_)
                    print(nome)
                else:
                    print("Valor incorreto, Digite novamente!")
    elif entrada in ["nao", "não"]:
        print("Saindo do sistema...")
        break