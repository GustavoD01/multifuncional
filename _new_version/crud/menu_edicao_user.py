def criar_usuarios():
    lista_geral_users = []
    while True:
    qtd_user = input(("Digite os seguintes caracteres para:  Adicionar somente [1] pessoa ou para [2] ou mais pessoas ou [F]inalizar a inserção de usuários: ")).strip().lower()
    #######################
    #Inserção de 1 Usuário#
    #######################
    if qtd_user == '1':

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

def verifica_qtd_usuarios():
    ##############################################################
    #Verifica se os objetos dentro da Lista principal, são Listas#
    ##############################################################
    if isinstance(lista_geral_users[0], list):
    lista_a_recuperar_salva = [["", ""] for _ in lista_geral_users]
    #######################################
    #Lista com Listas - 2 ou mais Usuários#
    #######################################

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
    print("\n", 20 * "-" + "Lista com índices" + 20 * "-", "\n")
    indices = range(len(lista_geral_users))
    for indice in indices:
    print(f"Valor {lista_geral_users[indice]} está no índice: {indice + 1}")
    ########
    #Opções#
    ########
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão:\n ").strip().lower()
    indice_externo = ""

def menu_edicao_usuario():
    print("\n", 20 * "-" + "Lista" + 20 * "-")
    print(f'Nome: {lista_geral_users[0]}')
    print(f'Quantidade de água ingerida/dia: {lista_geral_users[1]}L')
    ########
    #Opções#
    ########
    entrada = input("\nDeseja [A]lterar, [R]ecuperar algum item digitado ou [N]ão: \n").strip().lower()

def recuperar_usuario():
    elif entrada == "r" and any(preenchida == ["", ""] for preenchida in lista_a_recuperar_salva):
    limpa_tela()
    print("Erro: A lista está vazia, não é possível recuperar nada!")

def recuperar_1_usuarios():
    elif entrada == "r":
    limpa_tela()
    print("Erro: Não existem valores a serem recuperados!")
    ###################
    #"NÃO" selecionado#
    ###################

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