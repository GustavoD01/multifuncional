A = "ÁGUA" #Se variável for maiúscula, significa que é imutável
B = ''
print(B.zfill(100))
print(id(A)) #ID da variável A

contador = 3
print(f'Iniciando programa em {contador}')
while contador > 0:
    contador -= 1
    if contador == 2:
        print("Não vou mostrar o 2")
        continue
    print(f'Iniciando programa em {contador}')
    

print("BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'%s💧 \n\n"% (A)) #Variável string
print(A[0])
print(A[-3])
print(A[2])
print(A[-1])

print("\n", A[::-1] ,"\n") #inverter string
permissao = False

while permissao == False:
    entrada = input("\n\n Deseja entrar no sistema? (Sim ou Não)").strip().lower() #startswith('s') -> retorna bool de acordo com inicio da palavra e tem o endswith que também retorna bool porém com fim da palavra
    if entrada == True:
        print("\nCrie um Usuário e Senha")
        usuario_permitido = input("Crie seu Usuário: ")    
        senha_permitida = input("Crie sua senha: ")

        print("ÁREA DE LOGIN:")
        permissao = False
        
        while permissao == False:
            usuario = input("Digite seu Usuário: ")
            senha = input("Digite sua senha: ")
            if (usuario == usuario_permitido or usuario == "admin") and \
            senha == senha_permitida:
                permissao = True
                qtd_agua = 0
                string = 'b={nome2} a={nome1}'
                formato = string.format( #quando uma função está dentro de um objeto é chamada de método
                    nome1=A, nome2=qtd_agua #parâmetros
                )
                print(50 * "_")
                print("\nSeja bem vindo ao controle de água 💧 \n")
                print("Curiosidade: a palavra", A,"é um(a)", type(A))
            
                #try:
                qtd_agua = input("informe quantos litros de água você bebeu até agora: ")
                
                #except:
                    #print("Valor incorreto")
                if qtd_agua.isdigit():
                    agua = int(qtd_agua)
                    print("Parabéns, sua quantidade de água foi alocada corretamente no sistema")
                    print("Parabéns, você bebeu ", agua , " litros de água até agora")
                    print("Em hexadecimal você bebeu", f'{agua:08X}')
                    print("Por hora você bebeu ", f'{agua/24:.2f}', " água")
                else:
                    print("Valor incompatível, digite um valor correto. Exemplo: 2")
            else:
                print("Usuário ou senha incorreta, tente novamente")
    elif entrada == "não" or entrada == "nao":
        print("Saindo do sistema...")
        break
    else:
        print("Digite Sim ou Não: ")