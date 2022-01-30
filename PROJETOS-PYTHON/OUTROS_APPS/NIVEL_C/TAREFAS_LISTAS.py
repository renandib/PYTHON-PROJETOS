## EXIBINDO PROGRAMA QUE TRABALHE COM LISTAS

lista =list()

while True:
    valores = int(input("digite um valor para add na lista "))
    if valores not in lista:
        lista.append(valores)
        print("valor adicionado na lista")
    else:
        print("Valor ja existe, não sera adicionado")
    resp=input("Quer continuar S/N")
    if resp == "n":
        break

lista.sort()
print(f'Os valores add em ordem cresc são: {lista}')

#### 2° PROGRAMA ==

#### ====> CRIANDO AS LISTAS VAZIAS PARA RECEBER OS VALORES DPS
lista=list()   # LISTA D TODOS OS N° Q EU VOU DIGITAR
par=list()
impar=list()
print("Digite varios n° e no final obtenha os n° pares / impares / e todos q vc digitou ")
while True:  # looping pra manter o programando girando  > LEMBRANDO Q ELE VAI EXECUTAR TODAS AS CONDIÇÕES. ELE SÓ PARA QUANDO A RESP == S
    num=int(input("Digite um n°: "))
    lista.append(num)  #CADA VEZ Q VC DIGITAR UM N° ELE JA VAI ADD DENTRO DA LISTA > ATRAVES DO METODO APPEND
    if num%2==0:      # SE FOR PAR JA VAI ADICIONAR NA LISTA PAR
        par.append(num)
    else:               # SE NÃO FOR PAR ELE VAI ADD NA LISTA IMPAR
        impar.append(num)
    resp=input("Digite [S] para continuar ou Qualquer outra coisa para sair e OBTENHA AS RESPOSTAS: ")  # AQUI EU ESTOU FAZENDO UM METODO DE PARAR O PROGRAMA > ELE N TA DENTRO DO ELSE
    if resp!="s":  # SE O QUE EU DIGITAR ACIMA FOR DIFERENTE DE "S" ELE PARA O PROGRAMA COM O BREAK EMBAIXO.. SE NÃO.. ELE CONTINUA RODANDO O LOOPING
        break
print(f'Os valores pares são {par}. Os valores impares são {impar}. e os n° digitados foram > {lista}')

#print('Os valores da lista é {0} :' .format(lista))

#print('os valores pares são: {1}'.format(par))

#print('os valores impares são:{2} '.format(impar))



###### 3° PROGRAMA == TAREFA DE FIBONACCI

# Inplemente um código em Python para uma função recursiva de Fibonacci

# É UMA SEQUÊNCIA QUE A PARTIR DO 3° TERMO=1 , SOMA-SE +1 E VAI GERANDO UMA SEQUÊNCIA DE NUMEROS.

# EX BASICO DE UMA SEQUENCIA FIBONACCI > [ 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , ...... ]

# DIGITE UM N° ENTRE 2 ATÉ 50 E VEJA A SEQUÊNCIA FIBONACCI QUE SERÁ CRIADA.

num=int(input("Escolha um n° entre [ 3 até 50 ] e obtenha a sequência de fibonacci "))

n1=0  # PADRÃO 1° TERMO
n2=1  # PADRÃO 2° TERMO
cont=3  # A PARTIR DO 3° TERMO QUE COMEÇA MUDAR> ENTAO TENHO Q FALAR Q MEU CONTADOR COMEÇA DAQUI > COMO SE FOSSE O INICIO
sequenc=[]  # CRIANDO UMA LISTA VAZIA PARA ADD O RESTANTE DOS N° PARA A SEQUENCIA

while (num>=3 or num<=50):    # SE O N° Q ESCOLHER FOR MAIOR Q 3 OU MENOR Q 50 ELE JA VAI GERAR O LOOP > CASO CONTRARIO ELE PARA O PROGRAMA
    if(num>=cont and num<=50):          # SE NUM FOR MAIOR Q CONT ELE VAI GERAR A SEQUENCIA E VAI ADICIONAR NO N3 A CADA VOLTA UM N° GERADO/ se num for maior q 50 da erro
        n3=n1+n2         # O VALOR PADRÃO > N3 = 0+1 >> N3=1 ... A 1° VEZ ......GORA FALTA O RESTANTE
        n1=n2           # N1=N2 > 0 = 1  >> N2=1  >>N1=1
        n2=n3           # N2 = N3 >> 1 = 1
        cont += 1     # QUANDO VOLTAR LA ENCIMA DENOVO 2° VOLTA > N3=1+1 >> N3=2 E ASSIM SUCESSIVAMENTE
                    # NA 3° VOLTA > N3 = 2 >> PORTANTO > N1=1  E N2=2  >> N3 = 1+2 >> N3=3
                    # NA 4° VOLTA > N3=3 >> N1=2 / N2=3  >> N3= 2+3  >> N3=5 .... E ASSIM VAI
        sequenc.append(n3)
    else:
        break

print("\n Segue a sequência de fibonacci : ")
print(f'0 => 1 => {sequenc} ')



def fatorial(n):
    n=int(input("Digite um n° e descubra o termo em fibonnaci! "))
    if n==0 or n==1:
        return 1
    else:
        return
        print(n* fatorial(n-1))





