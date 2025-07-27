UA" #Se variável for maiúscula, significa que é imutável
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

FRASE = "BEM VINDO AO CONTROLE DE INGESTÃO DIÁRIO D'%s💧 \n\n"% (A) #Variável string
print(FRASE)
print("A frase acima contém ", FRASE.count('A') ," carateres 'A' que foram contados com o método count")
print(A[0])