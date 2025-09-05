def limpa_tela():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def curiosidades():
    A = "Corte"
    print("Curiosidade: a palavra", A,"é um(a)", type(A))
    #
    # Caso possuir algum número com ponto flutuante muito grande, é adequado utilizar esta função
    # Exemplo: numero_2 = decimal.Decimal(0.7)
    #
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
    A = "Corte"
    ##############
    #Tela Inicial#
    ##############
    FRASE = "TELA INICIAL ✂️ \n\n"% (A) #Variável string constante
    frase_separada = FRASE.split(" ")
    print(frase_separada)
    print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
    print(A[0])
    print(A[-4])
    print(A[2])
    print(A[-2])
    print(A[4])
    print("\n", A[::-1] ,"\n") #inverter string

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