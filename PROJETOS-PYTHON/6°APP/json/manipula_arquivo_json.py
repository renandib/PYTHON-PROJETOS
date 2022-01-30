### APP DE MANIPULAÇÃO DE JSON

# VIDEO DO APP ==> https://www.youtube.com/watch?v=9XObUQcVeIY&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=9

## importando todas as funcoes  q eu criei ===> FUNCOES_JSON sempre é bom olhar la nas funcoes pra entender o que fez

from json.funcao_json import *

# VERIFICANDO SE TEM OU NAO O ARQUIVO==> OBS ==> SE JA TIVER, ELE VAI MANTER O QUE TEM E VAI ADD AS COISAS NOVAS, CASO CONTRARIO SÓ VAI ADD COISA NOVAS
inventario = ler_arquivo("inventario_json.json")

opcao=chamarMenu() # CHAMANDO AS OPÇÕES DO MENU

cont = "S"
while opcao==1 or opcao==2 or opcao > 3 or cont =="S" :
    if opcao==1:
        # DANDO PRINT DA FUNCAO DE CRIAR O ARQUIVO E TBM PREENCHE-LO
        print(registrar(inventario, "inventario_json.json")) # atraves do metodo [dump] ==> dicionario , arquivo
    elif opcao==2:
        # USANDO A FUNCAO EXIBIR= => PRA EXIBIR TUDO DO ARQUIVO Q EU CRIEI EM JSON
        exibir("inventario_json.json")
    else:
        print("opção inválida, digite as duas opções que são validas")

    cont = input("Deseja continuar digite [S].").upper()
    if cont == "S" :
        opcao = chamarMenu()

    else:
        print("Obrigado por finalizar o programa")
        break

## PRONTO TERMINEI MANIPULAÇÃO DE ARQUIVOS

# LEMBRANDO Q VAI GERAR O ARQUIVO ==> INVENTARIO_JSON.JSON
