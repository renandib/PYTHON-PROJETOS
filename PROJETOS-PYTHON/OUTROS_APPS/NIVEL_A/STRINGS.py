### PEQUENOS PROGRAMAS UTILIZANDO MANIPULAÇÃO DE STRINGS

mensagem="Etec de embu"

print(len(mensagem))  ## VAI MOSTRAR QUANTOS CARACTER TEM A MENSAGEM = 12

print(mensagem[0:5])# vai imprimir sómente > etec >  lembrando que a ultima posição ele não imprimi.. tenq colocar 1 maior

print(mensagem[:7])  # docomeço até a posicao 6

print(mensagem[7:])  # da posicao 7 até o final

print(mensagem[-1])  # ele conta do final da direita para esquerda

print(mensagem[0:-2]) # vai escrever tudo porem vai tirar menos 2 do final

# 1)  Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
print("Digite 2 numeros, e ao final você terá a soma dos dois!")

num1=int(input("Digite o 1°n: "))
num2=int(input("Digite o 2°n: "))

soma=(num1+num2)

print(f'O 1°n foi de: [{num1}]. O 2° n foi de: [{num2}]. A soma dos dois numeros é de: [{soma}]')

# ===================================================================================================

# 2)  Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
num=float(input('digite a medida em metros e obtenha o resultado em milimetros : '))

conversao=num*1000

print(f' O valor da medida foi de: [{num}(m)]. Convertendo em milimetros fica: [{conversao}(mm)].')
# ========================================================================================================

# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos pelo usuário. Calcule o total em segundos.
dias=int(input("Digite a qnt de dias: "))
horas=float(input("Digite a hora: neste formato > 00.00 "))
minutos=float(input("Digite os minutos: neste formato > 00.00 "))
segundos=float(input("Digite os segundos: neste formato> 00.00 "))

conta1=(dias*86400)  # vai mostrar quantos segundos tem cada dia
conta2=(horas*3600)  # vai mostrar quantos s tem cada hora
conta3=(minutos*60)  # vai mostrar quantos s tem cada min
conta4=(conta1+conta2+conta3+segundos)  # vai mostrar o total geral de segundos de cada dado coletado

print(f'A Qnt de dias foi de: [{dias}(d) = {conta1}(s)]. A qnt de horas foram: [{horas}(h) = {conta2}(s)].'
      f' Os minutos foram de: [{minutos}(m) = {conta3}(s)]. E os segundos foram: [{segundos}(s)]. O valor total em (s) é de: [{conta4}(s)]')
#==============================================================================================================

# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e o valor do novo salário.
salario=float(input("Digite o seu salario. Após isso, você verá o novo salário com um aumento na % escolhida. "))

porcent=float(input("Digite a porcentagem de aumento : % "))

conta=(salario*porcent)/100 # > vai mostrar o aumento que teve

conta2=(conta+salario)  # > vai mostrar o novo salario com aumento

print(f' Seu salário inicial era de: [{salario} (R$)]. Teve um aumento de [{porcent}(%) = {conta}(R$)].'
      f' Seu novo salário será de: [{conta2} (R$) ].')
#=====================================================================================================

# 5) Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
compra=float(input("Digite o valor do produto e obtenha o desconto com o percentual escolhido: R$ 00.00 "))

porcent=float(input("Digite o valor da porcentagem de desconto (%) : "))

conta=(compra*porcent)/100  # valor do desconto

conta2=(compra-conta) # valor final com desconto

print(f' O valor inicial do produto é de: [{compra} (R$)]. A porcentagem de desconto foi de: [{porcent} (%)].'
      f' O valor final do produto com desconto é de : [{conta2} (R$)].')
#====================================================================================================

# 6) Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia=float(input("Digite a distancia percorrida em km: "))

velocidade=float(input("Digite a velocidade média percorrida em km/h: "))

conta=(distancia/velocidade)*3600 # vai descobrir o tempo em (S)

print(f' A distancia percorrida foi de: [{distancia} (km)]. A velocidade média foi de: [{velocidade} (Km/h)]'
      f' Portanto o tempo gasto foi de: [{conta} (s)].')
#===================================================================================================

# 7) Exiba um programa que converta uma temperatura digitada em “C” para “F” (Celsius para Fahrenheit).
temp1=float(input("Digite a temperatura em graus C°. E obtenha o valor em F° : "))

conta=(temp1*1.8)+32  # > formula para transformar graus c° em f°

print(f' O valor da temperatura em graus C° é de: [{temp1} (C°)]. Transformando em F° fica: [{conta} (F°)]')

#===============================================================================================

# 8) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

dias=float(input("Digite a qnt de dias do aluguel do carro: "))
km=float(input("Qual a qnt de km percorrido ? "))

conta1=(dias*60)  # mostrará o valor total das diarias do carro

conta2=(km*0.15)  # mostrara o valor total por todos km rodado

conta3=(conta1+conta2) # valor final de todas diarias + o km
print(f' A Qnt de diarias do carro foi de: [{dias}(d)]. ( O valor diario + o km rodado é de : 60,00 + 0.15 R$ )'
      f' Portanto o valor total da suas diarias + o km rodado é de: [{conta3}(R$)] ')