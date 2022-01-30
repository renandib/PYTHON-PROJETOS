## 1° ) RESUMO SOBRE LISTAS == > ARRAY

# PARA COMENTAR UTILIZE ==> [#] OU """ COMENTARIO """

## =========== CRIANDO LISTA
carros = ["hrv","golf","argo","fox"]

## =========== ENCONTRANDO LISTA POR INDICE

"""
print(carros[0]) ##==> HRV

print(carros[-1]) ##==> FOX

print(carros) ##==> ['hrv', 'golf', 'argo', 'fox']
"""
## ========== ADICIONANDO ELEMENTOS NA LISTA ===> METODO [APPEND] ==> ADD ITEM A ULTIMA POSICAO

#carros.append("fit")

#print(carros) ##==> ['hrv', 'golf', 'argo', 'fox' , 'fit']

## ============ VERIFICANDO O TAMANHO TOTAL DA LISTA ==> METODO [ LEN (LISTA) ]

#print(str(len(carros)) + " carros dentro da lista") ##=> 7 carros dentro da lista

## ============== REMOVENDO ITENS DA LISTA  ===> METODO [ REMOVE ]

#carros.remove("fit") ##==> obs se tentar remover um carro q nao existe ==> ele da erro
#print(carros)

## ============= REMOVENDO O [ULTIMO ITEM DA LISTA ] ===> METODO [ POP ]
"""
print(carros)
carros.pop() ##==> remove o argo
print(carros)
"""
## =========== REMOVENDO ITENS POR POSIÇÃO DA LISTA ===> METODO [ DEL ]
"""
print(carros)
del carros[2]
print(carros)
"""
## ============= PARA LIMPAR A LISTA TODA DE UMA VEZ SÓ É SÓ USAR O METODO [ CLEAR ]
"""
carros.clear() ##==> apaga toda a lista  de uma vez
print(carros)
"""
## ============== PASSANDO TODA UMA LISTA PARA DENTRO DE OUTRA

#carros2 = list(carros) ##==> dessa maneira atraves do casting ==> passa tudo q dentro da lista [carros] pra lista carros2
#print(carros2)

## ====== *** TRABALHANDO COM MATRIZES == > [LISTAS DENTRO DE LISTAS ]

carros3 = [
    ["modelo","hrv"],
    ["Fabricante","honda"],
    ["Ano","2016"]
]

#print(carros3[2][0]) ##==> Ano

### OUTRA MANEIRA DE IMPRIMIR

for l , c in carros3 :
    print("linha : " , l)
    print("coluna : " , c)

############## ++ ################ +++ ###################3


