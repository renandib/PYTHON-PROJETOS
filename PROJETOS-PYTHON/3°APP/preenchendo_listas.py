### ======> PREENCHENDO LISTAS DE EQUIPAMENTOS EM UMA LISTA

## VIDEO DO APP ==> https://www.youtube.com/watch?v=qjPhI_PShF0&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=4

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite "+'S'+" para continuar: ").upper()

## PREENCHENDO AS LISTAS

for indice in range(0,len(equipamentos)):  # sempre é bom quando quiser contador usar o for variavel in range(0,len(lista) )
  print("Equipamento..: ", (indice+1)) ## vai começar em 1 o contador
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])



### DESAFIO 2 - PESQUISANDO ITENS DENTRO DE LISTAS ( USANDO FOR DE CIMA) =>IMPRESSORA VAI GANHAR 10 % DE DESCONTO

busca = input("Digite o nome do equipamento que deseja buscar e veja se possui desconto : ")

if busca == equipamentos[indice] and busca == "impressora":

        conta = valores[indice] * 0.9
        print('Impressora está com desconto de 10 %')
        print("Valor..: ", conta)
        print("Serial.:", seriais[indice])

else:
    print('Equipamento não encontrado')


## DESAFIO 3 - DELETANDO UM ITEM ATRAVES DE UM SERIAL DA LISTA
serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]

        print(f'O equipamento {serial} foi excluido!')

    else:
        print(f'O serial {serial} não existe')
    break

## CONFERINDO SE FOI REALMENTE EXCLUIDO ==> MOSTRANDO DENOVO OS EQUIPAMENTOS Q SOBROU DPS DA EXCLUSAO..
for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])



"""PESQUISANDO ITENS DENTRO DE LISTAS ( USANDO FOR SEPARADO )

busca=input("Digite o nome do equipamento que deseja buscar e veja se possui desconto : ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])
print('Equipamento nao encontrado')
"""

