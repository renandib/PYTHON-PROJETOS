# 3°)
# AS FUNÇÕES DO NOSSO PROGRAMA JA FORAM CRIADOS NO ARQUIVO > (preenchendo_relatorios..)

# AGORA SÓ VOU FAZER A CHAMADA DELAS AQUI #

from dicionario.funcoes_inventario import *


usuarios={} # criando dicionario vazio

opcao=perguntar()  # CHAMANDO AS OPÇÕES DO MENU

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" or opcao == "S" or opcao!="I" or opcao!="P" or opcao!="E" or opcao!="L" or opcao!="S":
    if opcao=="I":
        inserir(usuarios)
        print("USUÁRIO REGISTRADO COM SUCESSO\n",usuarios)  # só pra mostrar o que tem dentro do dicionario

    elif opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? ").upper())


    elif opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? ").upper())

    elif opcao == "L":
        listar(usuarios)

    ## para sair do programa
    elif opcao == "S":
        print("Até logo!")
        break

    else:
        print("Opção incorreta, por favor selecione a opção correta")

    opcao = perguntar() # obs é bom deixar aqui ==> pq como esta dentro do WHILE, TODA VEZ Q CORRESPONDER UMA LENTRA DAS CONDIÇÕES ACIMA ==> ELE PERGUNTARA DENOVO.. isso economiza de ficar colocando em cada funcao separada





