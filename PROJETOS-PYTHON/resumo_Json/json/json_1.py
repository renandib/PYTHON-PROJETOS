### 3° ) RESUMÃO DE JSON ==> É IGUAL UM DICIONARIO A UNICA DIFERENÇA É Q É DO TIPO JSON

# primeiro importa a biblioteca == > lembrando q só funciona se for em um pact json
import json

# =====> CRIA O ARQUIVO JSON
carros_json = '{"Marca":"Honda","Modelo":"Hrv","Cor":"Prata"}'

## =====> CRIANDO VARIAVEL PRA MOSTRAR O JSON EM FORMATO DE STRING

# ESQUEMAAA CHAVE ==> TRANSFORMAR O JSON EM UM [DICIONARIO] ATRAVES DO METODO ABAIXO. [LOADS]

## =======> MÉTODO [JSON.LOADS] ==> JA TRANSFORMA EM UMA [STRING] O JSON

teste = json.loads(carros_json)

#print(teste) # em formato de dicionario ==> {'Marca': 'Honda', 'Modelo': 'Hrv', 'Cor': 'Prata'}

#print(teste["Marca"]) ##=> honda

#### OBS TOP ==> CASO EU QUEIRA TRANSFORMAR UM [DICIONARIO] EM UM [JSON] ==> MÉTODO [ DUMPS ]

carros = {"Marca":"Honda"
    ,"Modelo":"Hrv",
   "Cor":"Prata"}

## =========> TRANSFORMANDO EM JSON O DICIONARIO atravées do MÉTODO [ DUMPS ]

#carro_json = json.dumps(carros , indent=3 ,separators=(": ","=") , sort_keys=True)
## ==> pronto agora transformou isso em um JSON #
# OBS 1)=> ESSE [INDENT=3] É O ESPAÇAMENTO DA IDENTAÇÃO
# OBS 2)==> [SEPARATORS] --> TROCA O ":" EM "=" ==> ENFIM TROCA OS SINAIS Q EU QUERO
# OBS 3)==> [SORT_KEYS] ==> ORDENA AS CHAVES EM ORDEM ALFABETICA
#print("Arquivo JSON / objeto JSON: ",carro_json)

## OBS ==> TRANSFORMANDO LISTAS EM JSON ==> MESMO ESQUEMA ==> VAI VIRAR UM [ARRAY JSON]
#carros_list = ["honda" , "ford" , "fiat" , "Gm" ]

#cars_json = json.dumps(carros_list)

#print(cars_json) ##=> ["honda", "ford", "fiat", "Gm"]

## =======> IMPRIMINDO ELEMENTOS DO JSON ==> MANIPULA IGUAL O DICIONARIO

"""
for c in teste :
    print(f'SOMENTE CHAVES : {c}') # só chave
    print(f'SOMENTE VALORES : {teste[c]}') # só valores
"""

## ======> IMPRIMINDO CHAVE E VALOR JUNTOS ATRAVES DO METODO [ITEMS()]
"""
for c , v in teste.items():
    print("Chaves : " , c)
    print("valores : " , v)

    # ou #for c in teste.items():
#           print(c)
"""
## ======> IMPRIMINDO SÓ VALOR ATRAVES DO METODO [GET] ==> Q PEGA AS [CHAVES]

#print(teste.get("Marca")) # ou print(teste.keys()) todas as chaves


## =======> CRIANDO OBJETO JSON E TRAZENDO OS RESULTADOS Q EU QUERO

jogador_j =' {"nome":"bruno","time":"aviadores","vivo":"True","energia":"100","mochila":["faca","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

## =======> CONVERTENDO PARA DICIONARIO ==> OU OBJETO

jogador = json.loads(jogador_j)

## 1) ache as CHAVES
"""
for c in jogador:
    print(c)
"""
## 2) ache os ITEMS [CHAVES E VALORES ]

"""
for c in jogador.items():
    print(c)
"""

## 3) SÓMENTE OS VALORES
for c in jogador.values():
    print(c)

# ou valores somente da chave MOCHILA
"""
for c in jogador:
    print(jogador["mochila"])
    break
"""
# ====> OU DA PRA ACHAR SOMENTE OS ITENS DA MOCHILA USANDO O METODO GET

#print(jogador.get("mochila"))

## 4) pegue SOMENTE AS HABILIDADES DA CHAVE [ AERONAVES ]

"""
for h in jogador["aeronaves"]:
    print(h["habilidade"])

"""
## 5) PEGUE O "TIPO" + "HABILIDADE" DA CHAVE [ AERONAVES ]
"""
for i in jogador["aeronaves"]:
    print(f'O tipo é : {i["tipo"]}\n  e a habilidade é : {i["habilidade"]}')
"""

##### OBS TOP == > AQUI ACIMA EU CRIEI UM ARQUIVO JSON AQUI MESMO

###### POREM SE EU TIVESSE Q PEGAR UM ARQUIVO [JSON] E TROUXER PRA CA FAZ ASSIM :


#with open ("caminho...//,r") as arquivo : ## chamando arquivo JSON DO MEU PC

   # jogador = json.load(arquivo) ## TRAZENDO ELE PRA CA COM O MÉTODO [LOAD]


## pronto FINALIZADO == > AGORA VOU FALAR SOBRE MANIPULAÇÃO DE ARQUIVOS

# DPS VOU FAZER O VIDEO DE ==> LISTAS , DICIONARIOS , JSON E MANIPULAÇÃO DE ARQUIVOS







