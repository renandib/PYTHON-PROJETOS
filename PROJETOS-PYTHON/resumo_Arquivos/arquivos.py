### 4° ) RESUMÃO DE MANIPULAÇÃO DE ARQUIVOS

## importanto biblioteca == re => pra usar na substituição la embaixo
import  re

# para poder excluir um arquivo

import os

# R - READ = LEIA
# A - APPEND = ADD
# W - WRITE = ESCREVA
# x - CREATE - CRIAR

## CRIANDO 1°ARQUIVO e ESCREVENDO (WRITE = W)
"""
with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "w") as arquivo :
    arquivo.write("criando 1° arquivo\n")

## LENDO UM ARQUIVO (READ = R)

with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "r") as arquivo :
    print(arquivo.read())


### ESCREVENDO UM NOVO TEXTO (APPEND = A ) NO ARQUIVO

with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "a") as arquivo :
    arquivo.write("novo texto add\n")
"""
## VERIFICANDO SE O TEXTO FOI ADICIONADO JUNTAMENTE COM O OUTRO TEXTO
"""
with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "r") as arquivo :
    print(arquivo.read())
"""
## LENDO LINHA POR LINHA DO ARQUIVO E GUARDANDO EM UMA LISTA ==> READLINES()
"""
with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "r") as arquivo:
    for l in arquivo:
        print(arquivo.readlines())
"""
#### SUBSTITUINDO  COISAS ISOLADAS Q EU QUERO ==> METODO [SUB]

 # lembrando q "\s" é espaços ==> entao vai substituir por "add"
 # (OBS SÓ VAI DAR CERTO SE FIZER ISSO EM UM PACKET JSON
"""
with open("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt", "a") as arquivo :
    arquivo.write("novo texto add\n")

       res = re.sub("\s","add",arquivo.readlines())

    print(res)
"""

### DELETANDO UM ARQUIVO

# 1° IMPORTA A BIBLIOTECA == > [OS]
"""
if os.path.exists("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt") :
    print("ARQUIVO EXISTENTE")

else :
    print("ARQUIVO NAO EXISTE ")
"""
## AGORA EXCLUINDO MESMO
if os.path.exists("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt") :
    os.remove("C:/Users/Renan/Desktop/PYTHON0-FIAP/arquivo.txt")
    print("ARQUIVO REMOVIDO")

else:
    print("Arquivo não ENCONTRADO, não foi removido")










### PRONTO , AGORA SÓ FAZER VIDEO DE LISTAS , DICIONARIOS , JSON , E MANIPULACAO DE ARQUIVOS

## DPS FAZER PROVA DA FIAP PYTHON - ORGANIZAR CADERNO , CURSO DE SQL E TBM ARQUIVOS PRO GIT E TBM LINKEDLIN

