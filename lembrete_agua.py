import sys
import os
import decimal
import copy

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
    jogar = input("Deseja jogar 'escolha um número?' ([S]im ou [N]ão): ").strip().lower()
    if jogar == "s":
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
    elif jogar == 'n':
#
#Acesso ao sistema
#
        jogo = False
while True:
    entrada = input("Deseja entrar no sistema? ([S]im ou [N]ão): ").strip().lower() #startswith('s') -> retorna bool de acordo com inicio da palavra e tem o endswith que também retorna bool porém com fim da palavra
    if entrada == 's':
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
            if os.name == "nt":
                            os.system('cls')
            else:
                os.system('clear')
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
                #Essa nova implementação possuirá "crud" baseado em listas, simulando as opreações básicas. Como se trata de List in List, será necessário captação de 2 índices
                #
                #Novo problema detectado, quando inserido apenas 1 pessoa, os índices internos acabam "virando" índices externos, solucionado da seguinte forma:
                #

                if lista_geral_users
                lista_a_recuperar_salva = [["", ""] for _ in lista_geral_users]

                while True:
                    print("\n", 20 * "-" + "Lista com índices" + 20 * "-")
                    indices = range(len(lista_geral_users))
                    for indice in indices:
                        print(f"Valor {lista_geral_users[indice]} está no índice: {indice + 1}")
                    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão:\n ").strip().lower()
                    indice_externo = ""

                    if entrada == "a":
                        indice_interno = ""
                        ##########################
                        #Pedindo índice "externo"#
                        ##########################
                        while True:
                            try:
                                indice_externo = int(input("Digite o índice desejado: "))
                                if indice_externo <= len(lista_geral_users):
                                    if os.name == 'nt':
                                        os.system('cls')  # Limpa tela no Windows
                                    else:
                                        os.system('clear')  # Limpa tela no Linux/Mac

                                    break
                                else:
                                    print("Erro: Índice maior do que a lista, tente outro por favor!")
                            except ValueError:
                                print("Erro: Por favor digite um tipo correto")
                            except IndexError:
                                print("Erro: Índice não existe na lista")
                            except Exception:
                                print("Erro: Erro Desconhecido")
                                
                        indice_externo = (indice_externo - 1)
                        print(f"Você selecionou '{lista_geral_users[indice_externo]}'")
                            #######################
                            #Pede índice "interno"#
                            #######################
                        while indice_interno not in [0, 1]:
                            deseja_alterar = input("Deseja alterar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
                            if deseja_alterar == "n":
                            ##############
                            #Alterar Nome#
                            ##############
                                indice_interno = 0
                                while True:
                                    nome_a_ser_alterado = input("Digite o nome desejado: ")
                                    if len(nome_a_ser_alterado) >= 3:
                                        lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
                                        del lista_geral_users[indice_externo][indice_interno]
                                        lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
                                        print("Valor alterado com sucesso!")
                                        # lista_enumerada = enumerate(lista_geral_users)
                                        break
                                    else:
                                        print("Erro: Nome deve possuir pelo menos 3 caracteres!")
                            
                            elif deseja_alterar == "q":
                            ####################
                            #Alterar Quantidade#
                            ####################
                                indice_interno = 1
                                while True:
                                    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
                                    if quantidade_a_ser_alterada.isdigit() == True: 
                                        lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
                                        del lista_geral_users[indice_externo][indice_interno]
                                        lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
                                        print("Valor alterado com sucesso!")
                                        print(lista_a_recuperar_salva)
                                        # lista_enumerada = enumerate(lista_geral_users)
                                        break
                                    else:
                                        print("Erro: Quantidade está incorreta")
                            elif deseja_alterar == "t":
                            ###############
                            #Alterar Todos#
                            ###############
                                indice_interno = 0
                                while True:
                                    nome_a_ser_alterado = input("Digite o nome desejado: ")
                                    if len(nome_a_ser_alterado) >= 3:
                                        lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
                                        del lista_geral_users[indice_externo][indice_interno]
                                        lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
                                        print("Valor alterado com sucesso!")
                                        indice_interno = 1
                                        break
                                    else:
                                        print("Erro: Nome deve possuir pelo menos 3 caracteres!")
                                print(lista_geral_users)
                                while True:
                                    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
                                    if quantidade_a_ser_alterada.isdigit() == True:
                                        del lista_geral_users[indice_externo][indice_interno]
                                        lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
                                        break
                                    else:
                                        print("Erro: Quantidade está incorreta!")
                            else:
                                print("Erro: Digite um valor válido!")
                        #######################
                        #Pede índice "interno"#
                        #######################
                    elif entrada == "r" and any(preenchida != ["", ""] for preenchida in lista_a_recuperar_salva):
                        indice_interno = ''
                        ##########################
                        #Pedindo índice "externo"#
                        ##########################
                        while True:
                            try:
                                indice_externo = int(input("Digite o índice desejado: "))
                                if indice_externo <= len(lista_geral_users):
                                    indice_externo = (indice_externo - 1)
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    break
                                else:
                                    print("E")
                            except ValueError:
                                print("Erro: Por favor, digite um tipo correto!")
                            except IndexError:
                                print("Erro: Índice não existe na lista")
                            except Exception:
                                print("Erro: Erro Desconhecido")
                        if len(lista_a_recuperar_salva[indice_externo][0]) >= 3 or lista_a_recuperar_salva[indice_externo][1].isdigit() == True:
                            while indice_interno not in [0, 1]:
                                deseja_alterar = input("Deseja recuperar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
                                if deseja_alterar == "n":
                                    indice_interno = 0
                                    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
                                        lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                                        print("Valor foi recuperado com sucesso!")
                                        # indices = range(len(lista_a_recuperar_salva))
                                        # for indice in indices:
                                        #     print(f"Valor {lista_a_recuperar_salva[indice]} está no índice: {indice + 1}")
                                        break
                                    else:
                                        if os.name == "nt":
                                                        os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Erro: O nome é o mesmo do atual!")
                                elif deseja_alterar == "q":
                                    indice_interno = 1
                                    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
                                        lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                                        print("Valor foi recuperado com sucesso!")
                                        # indices = range(len(lista_a_recuperar_salva))
                                        # for indice in indices:
                                        #     print(f'Valor {lista_a_recuperar_salva[indice]} está no índice: {indice + 1}')
                                        break
                                    else:
                                        if os.name == "nt":
                                                        os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Erro: A quantidade é a mesma da atual!")
                                elif deseja_alterar == "t":  
                                    indice_interno = 0
                                    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
                                        lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                                        print("Valor foi recuperado com sucesso!")
                                        indice_interno = 1
                                        if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
                                            lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
                                            print("Valor recuperado com sucesso!")
                                            break
                                        else:
                                            if os.name == "nt":
                                                            os.system('cls')
                                            else:
                                                os.system('clear')
                                            print("Erro: A quantidade é a mesma da atual!")
                                    else: 
                                        if os.name == "nt":
                                                        os.system('cls')
                                        else:
                                            os.system('clear')
                                        print("Erro: O nome é o mesmo do atual")
                                else:
                                    if os.name == "nt":
                                                    os.system('cls')
                                    else:
                                        os.system('clear')
                                    print("Erro: Digite um valor válido")
                        else:
                            print("Erro: Índice escolhido não possui quantidade e nome a recuperar!")
                        
                    elif entrada == "r" and any(preenchida == ["", ""] for preenchida in lista_a_recuperar_salva):
                        if os.name == "nt":
                                        os.system('cls')
                        else:
                            os.system('clear')
                        print("Erro: A lista está vazia, não é possível recuperar nada!")
                    elif entrada == "n":
                        break
                    else:       
                        print("Erro: Digite um valor válido")
#
#Nada a alterar 'Não'
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
    elif entrada == 'n':
        print("Saindo do sistema...")
        break