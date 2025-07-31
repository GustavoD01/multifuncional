import sys
import os

A = "ÁGUA" #Se variável for maiúscula, significa que é imutável
B = ''
print(B.zfill(100))
print(id(A)) #ID da variável A

#Contagem regressiva
contador = 3
print(f'Iniciando programa em {contador}')
while contador > 0:
    contador -= 1
    if contador == 2:
        print("Não vou mostrar o 2")
        continue
    print(f'Iniciando programa em {contador}')

FRASE = "BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'%s💧 \n\n"% (A) #Variável string
print(FRASE)
print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
print(A[0])
print(A[-3])
print(A[2])
print(A[-1])

print("\n", A[::-1] ,"\n") #inverter string

#Advinhar número de 0 a 5
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
    #Acesso ao sistema
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
                
            print(50 * "_")
            print("\nSeja bem vindo ao controle de água 💧 \n")
            print("Curiosidade: a palavra", A,"é um(a)", type(A))
            lista_nomes = []
            lista_nomes.append(input("informe quantos litros de água você bebeu até agora: "))

            while lista_nomes[0].isdigit() == False:
                print("Valor incompatível, digite um valor correto. Exemplo: 2")
                lista_nomes.pop()
                lista_nomes.append(input("informe quantos litros de água você bebeu até agora: "))
            else:
                while True:
                    valor_01 = input("informe seu nome: ")
                    if len(valor_01) >= 3:
                        lista_nomes.append(valor_01)
                        break
                    else:
                        print("Seu nome deve conter pelo menos 3 caracteres!")
                    #os.system('cls')
            indices = range(len(lista_nomes))
            
            for indice in indices:
                print(f"Valor {lista_nomes[indice]} inserido com sucesso no índice: {indice}")


        #Inserção código CRUD simples de lista
            lista_recuperar = []
            permissao = False
            while permissao == False:
                entrada = input("Deseja alterar/recuperar algum item digitado? (Digite 'Recuperar' ou 'Alterar' ou 'Não' ): ").strip().lower()
                if entrada == "alterar":
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
                                print("Nome: ", lista_nomes[1], ", quantidade de água ingerida: ", lista_nomes[0])
                                break
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
                elif entrada == 'recuperar':
                    if lista_recuperar == []:
                        print("Você não tem valores a recuperar, insira uma opção válida")
                    else:
                        valor_a_recuperar = input("Digite o que deseja recuperar ('1' - Quantidade, '2' - Nome ou 'TODOS'): ").strip().lower()
                        while True:
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
                            else:
                                print("Digite '1' ou '2'!")
                                continue
                elif entrada in ["não", "nao"]:
                    permissao = True
                    print(lista_nomes)
                    agua = int(lista_nomes[0])
                    print("Parabéns ", lista_nomes[1], " sua quantidade de água foi alocada corretamente no sistema")
                    print("Parabéns, você bebeu ", agua , " litros de água até agora")
                    print("Em hexadecimal você bebeu", f'{agua:08X}')                        
                    print("Por hora você bebeu ", f'{agua/24:.2f}', " água")
                else:
                    print("Valor incorreto, Digite novamente!")
    elif entrada in ["nao", "não"]:
        print("Saindo do sistema...")
        break