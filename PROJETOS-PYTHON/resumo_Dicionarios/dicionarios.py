### 2°)  RESUMÃO SOBRE DICIONARIOS

## =======> BASICAMENTE É UMA LISTA , A UNICA DIFERENÇA É QUE TEM ===> CHAVE : VALOR

carros = {
    "Fabricante" : "honda" ,
    "Modelo" : "Hrv" ,
    "Ano" : "2017" ,
    "Cor" : "Prata"
}

## ========> ACESSANDO VALORES DO DICIONARIO

#print(carros) ##-==> {'Fabricante': 'honda', 'Modelo': 'Hrv', 'Ano': '2017', 'Cor': 'Prata'}

## ==========> QUANDO EU QUERO ACESSAR O [VALOR DA CHAVE] BASTA EU IMPRIMIR A CHAVE

#print(carros["Fabricante"]) ## acessando diretamente o INDICE [ CHAVE ]
#print(carros.get("Fabricante")) ## ACESSANDO a [CHAVE] PELO METODO [ GET] E OBTENDO O [VALOR]

## =========> OUTRA MANEIRA DE IMPRIMIR TODAS AS [CHAVES] OU [VALORES]

"""
for x in carros :
    print(carros[x])  # IMPRIMI TODOS OS [VALORES] == > print(x) ==> vai imprimir só [CHAVES]
"""
print(carros)
## ======> ou POSSO USAR ==> METODO [ KEYS ] == CHAVES   / [VALUES] == VALORES

#print(carros.keys()) ## TODAS AS CHAVES  ==> no formato de dicionario
#print(carros.values()) ## TODOS OS VALORES ==> no formato de dicionario


## =====>  METÓDOD [ITEMS] ==> IMPRIMI CHAVE E VALOR JUNTO == > EM FORMATO DE TUPLAS = LISTA

"""
for x in carros.items() :
    print(x) 
"""
# OU

"""
for c , v in carros.items() :
    print("chave ", c)
    print("valor ", v)
"""

## =====> ENCONTRANDO ITENS DENTRO DO DICIONARIO
# EX SIMPLES

#if "Modelo" in carros :
#    print("Modelo é uma chave do dicionario carros ")


## ======>  ADICIONANDO VALORES NO DICIONARIO

carros["Cambio"] = "automatico" ## "CHAVE" : VALOR ==> isso aqui vai add na ultima posicao do dicionario

## ======> DELETANDO ITENS DO DICIONARIO

#carros.pop("Cambio") ## USANDO METODO [POP] informo o valor

#del carros["Cambio"] ## USANDO METODO [DEL] INFORMO A POSIÇÃO

## ======> CRIANDO UM DICIONARIO DENTRO DE OUTRO


carros2 = {
    "Carro1" : {
        "Fabricante" : "Honda" ,
        "Modelo" : "Hrv"
    },

    "Carro2" : {
        "Fabricante" : "Volkswagen",
        "Modelo" : "fox"
    },

    "Carro3" : {
        "Fabricante" : "Ford" ,
        "Modelo" : "Focus"
    }
}

## ======> acessando QUERO IMPRIMIR O MODELO FOCUS

print(carros2["Carro3"]["Modelo"])  ## OU ==> print(carros2.get("Carro3").get("Modelo"))  == FOCUS


## =====> OBS TBM POSSO COLOCAR UM DICIONARIO DENTRO DO OUTRO ASSIM
"""
#carros1 = {}
#carros2 = {}

carros_geral = {
    "c1" : carros1,
    "c2" : carros2
}

print(carros_geral["c1"]) ## vai imprimir tudo q tem no dicionario de chave ==> c1 E ASSIM POR DIANTE

"""


