lista_nomes = [4, "teste"]
permissao = False
while permissao == False:
    entrada = input("Deseja alterar/excluir algum item digitado? (Sim ou Não): ").strip().lower()
    if entrada == "sim":
        while True:
            valor_a_alterar = input("Digite o número do que deseja alterar? (1 = Quantidade e 2 = Nome)")
            if valor_a_alterar == "1":
                print("Você digitou 1")
                break
            elif valor_a_alterar == "2":
                print("Você digitou 2")
                break
            else:
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