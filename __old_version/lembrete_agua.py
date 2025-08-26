import sys
import os
import decimal
import copy

#import decimal
#
# Caso possuir algum número com ponto flutuante muito grande, é adequado utilizar esta função
# Exemplo: numero_2 = decimal.Decimal(0.7)
#

def limpa_tela():
    if os.name == "nt":
    os.system('cls')
    else:
    os.system('clear')

def curiosidades():
    A = "Corte" #Se variável for maiúscula, significa que é imutável
    B = ''
    print(B.zfill(100))
    print(id(A)) #ID da variável A
    frase_unida = '-'.join("abc")
    print(frase_unida)

def contagem_regressiva():
    #####################
    #Contagem regressiva#
    #####################
    contador = 3
    print(f'Iniciando programa em {contador}')
    while contador > 0:
    contador -= 1
    if contador == 2:
    print("Não vou mostrar o 2")
    continue
    print(f'Iniciando programa em {contador}')

def tela_inicial():
    ##############
    #Tela Inicial#
    ##############
    FRASE = "TELA INCIAL ✂️ \n\n"% (A) #Variável string constante
    frase_separada = FRASE.split(" ")
    print(frase_separada)
    print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
    print(A[0])
    print(A[-4])
    print(A[2])
    print(A[-2])
    print(A[4])

    print("\n", A[::-1] ,"\n") #inverter string

##############
#Jogo Números#
##############

def advinhe_o_numero():
    print(20 * "-", "⚅ Advinhe o número ⚅", 20 * "-", "\n")
    usuario_permitido = ""
    senha_permitida = ""
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
    ################
    #Início sistema#
    ################

    print("\n", 20 * "-", "Entrada no sistema", 20 * "-", "\n")
    user_senha_correta = False
    jogo = False

def fazer_login():
    while True:
    entrada = input("Deseja entrar no sistema? ([S]im ou [N]ão): ").strip().lower() #startswith('s') -> retorna bool de acordo com inicio da palavra e tem o endswith que também retorna bool porém com fim da palavra
    if entrada == 's':
    limpa_tela()
    #########################
    #Criação Usuário e Senha#
    #########################
    print("\n", 20 * "-", "Área de login", 20 * "-")
    print("\nCrie um Usuário e Senha")
    while user_senha_correta == False:
    while len(usuario_permitido) < 3 or len(senha_permitida) < 3:
    usuario_permitido = input("Crie seu Usuário: ").strip().lower()
    senha_permitida = input("Crie sua senha: ")
    if usuario_permitido == 's':
    user_senha_correta = True
    break
    elif len(usuario_permitido) >= 3 and len(senha_permitida) >= 3:
    break
    else:
    print("Digite um usuário ou senha com pelo menos 3 dígitos")
    ############
    #Área Login#
    ############
def inserir_usuario():
    print("ÁREA DE LOGIN:")
    while True and user_senha_correta == False:
    #######################
    #Login Usuário e Senha#
    #######################
    usuario = input("Digite seu Usuário: ").strip().lower()
    senha = input("Digite sua senha: ")
    if (usuario == usuario_permitido or usuario == "admin") and (
    senha == senha_permitida):
    # lista_nomes = 0
    # string = 'b={nome2} a={nome1}'
    # formato = string.format #quando uma função está dentro de um objeto é chamada de método
    # nome1=A, nome2=lista_nomes #parâmetros
    user_senha_correta = True
    break
    else:
    print("Usuário ou senha incorreto! Tente novamente!")
    #####################
    #Entrando no sistema#
    #####################
    limpa_tela()

def menu_principal():
    print("\n", 20 * "-", "Seja bem vindo ao controle para cabeleireiro ✂️", 20 * "-","\n")
    print("Curiosidade: a palavra", A,"é um(a)", type(A))
    #Caso a lista_nomes contivesse valores que nunca seriam alterados, seria desejável que criasse uma tupla
    #Formas de criar uma tupla:
    #lista_nomes = '1', 2, '3'
    #lista_nomes = ('1', 2, '3') -> uso de parênteses ao invés de
    ######################
    #Inserção de usuários#
    ######################

def criar_usuarios():
    lista_geral_users = []
    while True:
    qtd_user = input(("Digite os seguintes caracteres para:  Adicionar somente [1] pessoa ou para [2] ou mais pessoas ou [F]inalizar a inserção de usuários: ")).strip().lower()
    #######################
    #Inserção de 1 Usuário#
    #######################
    if qtd_user == '1':
def criar_1_usuario():
    lista_geral_users = []
    while True:
    ###############
    #Inserção Nome#
    ###############
    var_1 = input(("Digite o nome do seu cliente: "))
    if len(var_1) >= 3:
    lista_geral_users.append(var_1)
    print("Cliente inserido com sucesso!")
    break
    else:
    print("Nome deve conter pelo menos 3 caracteres!")
    while True:
    #####################
    #Inserção Quantidade#
    #####################
    var_2 = input(("Digite o corte realizado pelo cliente: "))
    if var_2.isdigit() == True: 
    lista_geral_users.append(var_2)
    print("Corte inserido com sucesso!")
    print(lista_geral_users)
    break
    else:
    print("Quantidade inserida incorreta!")
    ################################
    #Inserção de 2 ou mais Usuários#
    ################################
    elif qtd_user == '2':
def criar_2_usuarios():
    lista_geral_users = []
    while True:
    ##################
    #Inserção 1° Nome#
    ##################
    var_recebe = input(("Digite o nome do seu cliente: "))
    if len(var_recebe) >= 3:
    var_1 = var_recebe
    print("Cliente inserido com sucesso!")
    break
    else:
    print("Nome inserido deve conter pelo menos 3 caracteres!")
    while True:
    ########################
    #Inserção 1° Quantidade#
    ########################
    var_recebe = input(("Digite a quantidade de água ingerida pelo primeiro usuário : "))
    if var_recebe.isdigit() == True:
    var_2 = var_recebe
    print("Quantidade inserida com sucesso!")
    break
    else:
    print("Quantidade inserida está incorreta!")
    #################
    #Adição na Lista#
    #################
    lista_insercao_users = [var_1, var_2]
    lista_geral_users.append(lista_insercao_users)
    print(lista_geral_users)
    #############################
    #Inserção do segundo usuário#
    #############################
    while True:
    ##################
    #Inserção 2° Nome#
    ##################
    var_recebe = input(("Digite o nome do segundo usuário: "))
    if len(var_recebe) >= 3:
    var_1 = var_recebe
    print("Nome inserido com sucesso!")
    break
    else:
    print("Nome deve conter pelo menos 3 caracteres!")
    while True:
    ########################
    #Inserção 2° Quantidade#
    ########################
    var_recebe = input(("Digite a quantidade de água ingerida pelo segundo usuário: "))
    if var_recebe.isdigit() == True:
    var_2 = var_recebe
    print("Quantidade inserida com sucesso!")
    break
    else:
    print("Quantidade inserida está incorreta!")
    #################   
    #Adição na Lista#
    #################
    lista_insercao_users = [var_1, var_2]
    lista_geral_users.append(lista_insercao_users)
    print(lista_geral_users)
    #########################
    #Adicionar mais usuários#
    #########################
    while True:
    limpa_tela()
    print(lista_geral_users)
    continuar = input(("Deseja adicionar mais um usuário? [S]im ou [N]ão: ")).strip().lower()
    if continuar == 's':
    while True:
    ####################
    #Inserção novo Nome#
    ####################
    var_recebe = input(("Digite o nome do novo usuário: "))
    if len(var_recebe) >= 3:
    var_1 = var_recebe
    print("Nome inserido com sucesso!")
    break
    else:
    print("Nome inserido está incorreto!")
    while True:
    ##########################
    #Inserção nova Quantidade#
    ##########################
    var_recebe = input(("Digite a quantidade de água ingerida pelo novo usuário: "))
    if var_recebe.isdigit() == True:
    var_2 = var_recebe
    print("Quantidade inserida com sucesso!")
    break
    else:
    print("Quantidade inserida está incorreta!")
    ###################
    #Adicição na Lista#
    ###################
    lista_insercao_users = [var_1, var_2]
    lista_geral_users.append(lista_insercao_users)
    elif continuar == 'n' and len(lista_geral_users) > 0:
    break
    else:
    print("Valor inválido, Tente Novamente!")
    ####################
    #Finalizar Inserção#
    ####################
def finalizar_criacao_usuario():
    elif qtd_user == 'f':
    if len(lista_geral_users) <= 1:
    print("Lista está vazia, digite um ou mais usuários para iniciar o programa")
    else:
    print("\n\n", lista_geral_users, "\n")
    break
    else:
    print("Valor inválido, Tente Novamente!")
    continue

############################
#Apresentar como Lista está#
############################

#                  *****************************************************************************************************************************************************************
#                  *Essa nova implementação possuirá "crud" baseado em listas, simulando as opreações básicas. Como se trata de List in List, será necessário captação de 2 índices*
#                  *****************************************************************************************************************************************************************
#                  *Novo problema detectado, quando inserido apenas 1 pessoa, os índices internos acabam "virando" índices externos, solucionado da seguinte forma:*
#                  *************************************************************************************************************************************************

def verifica_qtd_usuarios():
    ##############################################################
    #Verifica se os objetos dentro da Lista principal, são Listas#
    ##############################################################
    if isinstance(lista_geral_users[0], list):
    lista_a_recuperar_salva = [["", ""] for _ in lista_geral_users]
    #######################################
    #Lista com Listas - 2 ou mais Usuários#
    #######################################
    while True:
def menu_edicao_usuario():
    print("\n", 20 * "-" + "Lista com índices" + 20 * "-", "\n")
    indices = range(len(lista_geral_users))
    for indice in indices:
    print(f"Valor {lista_geral_users[indice]} está no índice: {indice + 1}")
    ########
    #Opções#
    ########
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão:\n ").strip().lower()
    indice_externo = ""
def alterar_2_usuarios():
    ###############################
    #Verifica se entrada é ALTERAR#
    ###############################
    if entrada == "a":
    indice_interno = ""
    ##########################
    #Pedindo índice "externo"#
    ##########################
    while True:
    try:
    indice_externo = int(input("Digite o índice desejado: "))
    if indice_externo <= len(lista_geral_users) and indice_externo > 0:
    limpa_tela()
    break
    else:
    limpa_tela()
    print("Erro: Índice está fora de range, tente outro por favor!")
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
    limpa_tela()
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
    limpa_tela()
    print("Valor alterado com sucesso!")
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
    ##############
    #Alterar Nome#
    ##############
    nome_a_ser_alterado = input("Digite o nome desejado: ")
    if len(nome_a_ser_alterado) >= 3:
    lista_a_recuperar_salva[indice_externo] = copy.deepcopy(lista_geral_users[indice_externo])
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, nome_a_ser_alterado)
    limpa_tela()
    print("Valor alterado com sucesso!")
    indice_interno = 1
    break
    else:
    print("Erro: Nome deve possuir pelo menos 3 caracteres!")

    print(lista_geral_users)
    while True:
    ####################
    #Alterar Quantidade#
    ####################
    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
    if quantidade_a_ser_alterada.isdigit() == True:
    del lista_geral_users[indice_externo][indice_interno]
    lista_geral_users[indice_externo].insert(indice_interno, quantidade_a_ser_alterada)
    limpa_tela()
    print("Valor alterado com sucesso!")
    break
    else:
    print("Erro: Quantidade está incorreta!")
    #################################
    #Verifica se entrada é RECUPERAR#
    #################################
def recuperar_2_usuarios():
    elif entrada == "r" and any(preenchida != ["", ""] for preenchida in lista_a_recuperar_salva):
    indice_interno = ''
    ##########################
    #Pedindo índice "externo"#
    ##########################
    while True:
    try:
    indice_externo = int(input("Digite o índice desejado: "))
    if indice_externo <= len(lista_geral_users) and indice_externo > 0:
    indice_externo = (indice_externo - 1)
    limpa_tela()
    break
    else:
    print("Erro: Índice está fora de range!")
    except ValueError:
    print("Erro: Por favor, digite um tipo correto!")
    except IndexError:
    print("Erro: Índice não existe na lista")
    except Exception:
    print("Erro: Erro Desconhecido")
    ###################################
    #Verifica se índice não está vazio#
    ###################################
    if len(lista_a_recuperar_salva[indice_externo][0]) >= 3 or lista_a_recuperar_salva[indice_externo][1].isdigit() == True:
    while indice_interno not in [0, 1]:
    deseja_alterar = input("Deseja recuperar o [N]ome, [Q]uantidade ou [T]odos: ").lower().strip()
    if deseja_alterar == "n":
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou nome não é igual#
    #######################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Valor foi recuperado com sucesso!")
    # indices = range(len(lista_a_recuperar_salva))
    # for indice in indices:
    #     print(f"Valor {lista_a_recuperar_salva[indice]} está no índice: {indice + 1}")
    break
    else:
    limpa_tela()
    print("Erro: O nome é o mesmo do atual!")
    elif deseja_alterar == "q":
    indice_interno = 1
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Valor foi recuperado com sucesso!")
    break
    else:
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual!")
    elif deseja_alterar == "t":  
    ###############
    #Alterar Todos#
    ############### 
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou nome não é igual#
    #######################################################
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Nome recuperado com sucesso!")
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    indice_interno = 1
    if lista_a_recuperar_salva[indice_externo][indice_interno] != lista_geral_users[indice_externo][indice_interno]:
    lista_geral_users[indice_externo][indice_interno] = lista_a_recuperar_salva[indice_externo][indice_interno]
    print("Quantidade recuperada com sucesso!")
    break
    else:
    #                                               ?????????????????????????????????????????????????????
    #                                               ?Repetição excessiva problema a ser resolvido no POO?
    #                                               ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual!")
    else:
    #                                            ?????????????????????????????????????????????????????
    #                                            ?Repetição excessiva problema a ser resolvido no POO?
    #                                            ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: O nome é o mesmo do atual")
    else:
    #                                        ?????????????????????????????????????????????????????
    #                                        ?Repetição excessiva problema a ser resolvido no POO?
    #                                        ?????????????????????????????????????????????????????
    limpa_tela()
    print("Erro: Digite um valor válido")
    else:
    print("Erro: Índice escolhido não possui quantidade e nome a recuperar!")
    ################################
    #Verifica se a Lista está vazia#
    ################################
def recuperar_usuario():
    elif entrada == "r" and any(preenchida == ["", ""] for preenchida in lista_a_recuperar_salva):
    limpa_tela()
    print("Erro: A lista está vazia, não é possível recuperar nada!")
    ###########################
    #Verifica se entrada é NÃO#
    ###########################
def saida_menu_edicao_usuario():
    elif entrada == "n":
    limpa_tela()
    break
    else:
    limpa_tela()
    print("Erro: Digite um valor válido")
    elif isinstance(lista_geral_users[0], list) == False:
    ############################################
    #Fim Implementação Lista 2 ou mais Usuários#
    ############################################
def verifica_qtd_usuarios():
    ################################
    #Implementação da Lista "Única"#
    ################################
    lista_a_recuperar_salva = ["", ""]

    indices = range(len(lista_geral_users))
    while True:
    if entrada != "n":
    entrada = ''
    else:
    break
    entrada_interna = ''
    indice_interno = ''
def menu_edicao_usuario():
    print("\n", 20 * "-" + "Lista" + 20 * "-")
    print(f'Nome: {lista_geral_users[0]}')
    print(f'Quantidade de água ingerida/dia: {lista_geral_users[1]}L')
    ########
    #Opções#
    ########
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão: \n").strip().lower()
    ###############################
    #Verifica se entrada é ALTERAR#
    ###############################
def alterar_2_usuarios():
    if entrada == "a":
    while True:
    # try:
    entrada_interna = input("Digite se você deseja alterar o [N]ome ou a [Q]uantidade: ").strip().lower()
    if entrada_interna == "n":
    indice_interno = 0
    ##############
    #Alterar Nome#
    ##############
    nome_a_ser_alterado = input("Digite o nome desejado: ")
    if len(nome_a_ser_alterado) >= 3:
    lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
    del lista_geral_users[indice_interno]
    lista_geral_users.insert(indice_interno, nome_a_ser_alterado)
    limpa_tela()
    print("Nome alterado com sucesso!")
    break
    else:
    print("Erro: O nome deve possuir pelo menos 3 caracteres!")
    continue
    elif entrada_interna == "q":
    indice_interno = 1
    ####################
    #Alterar Quantidade#
    ####################
    quantidade_a_ser_alterada = input("Digite a quantidade desejada: ")
    if quantidade_a_ser_alterada.isdigit() == True:
    lista_a_recuperar_salva[indice_interno] = copy.deepcopy(lista_geral_users[indice_interno])
    del lista_geral_users[indice_interno]
    lista_geral_users.insert(indice_interno, quantidade_a_ser_alterada)
    limpa_tela()
    print("Quantidade alterada com sucesso!")
    break
    else:
    print("Erro: A quantidade deve ser do tipo numérica!")
    continue
    else:
    print("Erro: Digite uma opção válida!")
    # except ValueError:
    #     print("Erro: Por favor digite um tipo correto!")
    # except IndexError:
    #     print("Erro: Índice não existe na lista")
    # except Exception:
    #     print("Erro: Erro Desconhecido")
def recuperar_2_usuarios():
    #################################
    #Verifica se entrada é RECUPERAR#
    #################################
    elif entrada == "r" and lista_a_recuperar_salva != ["", ""]:
    #                           ***********************************************************
    #                           *FUTURA ATUALIZAÇÃO É SAIR DO LOOP, CASO ENTRAR SEM QUERER*
    #                           ***********************************************************
    entrada_interna = input("Digite se você deseja recupera  o [N]ome ou a [Q]uantidade: ").strip().lower()
    if entrada_interna == 'n':
    ################
    #Recuperar Nome#
    ################
    indice_interno = 0
    #######################################################
    #Verifica se índice não está vazio ou Nome não é igual#
    #######################################################
    if lista_geral_users[indice_interno] != lista_a_recuperar_salva[indice_interno] and lista_a_recuperar_salva[indice_interno] != "":
    lista_geral_users[indice_interno] = lista_a_recuperar_salva[indice_interno]
    limpa_tela()
    print("Nome foi recuperado com sucesso!")
    else:
    limpa_tela()
    print("Erro: O nome é o mesmo do atual / ou não possui quantidade a ser recuperado!")
    elif entrada_interna == 'q':
    ######################
    #Recuperar Quantidade#
    ######################
    indice_interno = 1
    #############################################################
    #Verifica se índice não está vazio ou quantidade não é igual#
    #############################################################
    if lista_geral_users[indice_interno] != lista_a_recuperar_salva[indice_interno] and lista_a_recuperar_salva[indice_interno] != "":
    lista_geral_users[indice_interno] = lista_a_recuperar_salva[indice_interno]
    limpa_tela()
    print("A quantidade foi alterada com sucesso!")
    else:
    limpa_tela()
    print("Erro: A quantidade é a mesma da atual / ou não possui nome a ser recuperado!")
    else:
    print("Erro: Digite uma opção válida!")
    ##########################################
    #RECUPERAR selecionado, porém Lista vazia#
    ##########################################
def recuperar_2_usuarios():
    elif entrada == "r":
    limpa_tela()
    print("Erro: Não existem valores a serem recuperados!")
    ###################
    #"NÃO" selecionado#
    ###################
def saida_menu_edicao_usuario():
    elif entrada == "n":
    limpa_tela()
    print("Alterações Finalizadas!")
    break
    ################
    #Opção inválida#
    ################
    else:
    limpa_tela()
    print("Digite uma opção válida!")

    ###########################################################
    #Após "NÃO" ser selecionado, apresenta dados sobre a Lista#
    ###########################################################