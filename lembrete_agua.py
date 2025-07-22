a = "ÁGUA"

print("BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'ÁGUA💧 \n\n")
print(a[0])
print(a[-3])
print(a[2])
print(a[-1])

entrada = input("\n\n Deseja entrar no sistema? (Sim ou Não)").strip().lower()

if entrada == "sim":
    print("\nCrie um Usuário e Senha")
    usuario_permitido = input("Crie seu Usuário: ")    
    senha_permitida = input("Crie sua senha: ")

    print("ÁREA DE LOGIN:")
    usuario = input("Digite seu Usuário: ")
    senha = input("Digite sua senha: ")
    if (usuario == usuario_permitido or usuario == "admin") and senha == senha_permitida:
        qtd_agua = 0
        string = 'b={nome2} a={nome1}'
        formato = string.format( #quando uma função está dentro de um objeto é chamada de método
            nome1=a, nome2=qtd_agua #parâmetros
        )
        print(50 * "_")
        print("\nSeja bem vindo ao controle de água 💧 \n")
        print("Curiosidade: a palavra", a,"é um(a)", type(a))
        qtd_agua = float(input("informe quantos litros de água você bebeu até agora: "))

        if qtd_agua > 0:
            print("Parabéns, sua quantidade de água foi alocada corretamente no sistema")
            print("Parabéns, você bebeu ", qtd_agua , " litros de água até agora")
            print("Por hora você bebeu ", f'{qtd_agua/24:.2f}', " água")
        elif qtd_agua < 0:
            print("Quantidade de água inserida está incorreta")
        else:
            print("Valor incompatível, digite um valor correto. Exemplo: 2.14")
    else:
        print("Usuário ou senha incorreta, tente novamente")
elif entrada == "não" or entrada == "nao":
    print("Saindo do sistema...")
else:
    print("Digite Sim ou Não")