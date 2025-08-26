def criar_login():
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

def realizar_login():
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
