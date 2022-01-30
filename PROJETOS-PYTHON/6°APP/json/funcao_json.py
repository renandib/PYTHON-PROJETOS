### CRIANDO AS FUNÇÕES JSON ==> PARA O APP DE MANIPULAÇÃO JSON

#  LEMBRANDO Q TEM DOIS METODOS IMPORTANTES DO JSON :
# JSON.DUMP(LISTA/DICIONARIO , APELIDO DADO) ==> ADICIONA OS CONTEUDOS NO ARQUIVO
# JSON.LOAD(CARREGA OS DADOS DO ARQUIVO GERADO)

## CRIANDO AS FUNÇÕES PRA ROTINA Q EU QUERO FAZER  USANDO JSON ==> CRIANDO E MANIPULANDO MEU ARQUIVO

# 1° IMPORTA A BIBLIOTECA
import json

# 2° IMPORTA ESSE [OS = OPERACOES DE SISTEMAS] == > ELE VERIFICA SE JA NAO TEM ALGUM ARQUIVO PRA N DA BO
import os

# CRIANDO A 1° FUNCAO PRO MENU
def chamarMenu():
    escolha = int(input("Digite: ""<1> para REGISTRAR [PRODUTO]\n"
                      "<2> para exibir TODOS PRODUTOS armazenados: "))
    return escolha

## ANTES DE REGISTRAR E CRIAR UM ARQUIVO ==> EU PRECISO VERIFICAR SE JA TEM UM.. AI APROVEITA OS DADOS ANTIGOS.. OU ENTAO SOBREESCREVE UM NOVO

## CRIANDO A 2° FUNCAO PRA LER OS ARQUIVOS
def ler_arquivo(arquivo):
    # 1° VERIFICA SE O ARQUIVO EXISTE
    if os.path.exists(arquivo):
        # SE JA EXISTIR ELE SIMPLIMENTE VAI LER OS DADOS ==> E VAI MANTELOS - PRA EU CONTINUAR ADD ITENS SEGUINTES SEM SOBREESCREVER
        with open(arquivo, "r") as arq_json:
            dicionario=json.load(arq_json)
    else:
        # SE NAO EXISTIR O ARQUIVO ==> ELE VAI ESCREVER UM NOVO ==> UM DICIONARIO ZERADO
        dicionario = {}
    return dicionario

## PREENCHENDO DICIONARIO com o "W" + MÉTODO [DUMP]==> Q MANDA O CONTEUDO DO TEXTO ESCRITO PRO ARQUIVO EM JSON.

# 4° passo
# ANTES DE REGISTRAR O ARQUIVO => EU JA VOU CRIAR UMA FUNCAO ESPECIFICA , SÓ PRA SALVAR O TEXTO NO DICIONARIO OU ARQUIVO
def gravar_arquivo(dicionario,arquivo):
    with open(arquivo, "w") as arq_json: # ESCREVENDO NO ARQUIVO 1°
        json.dump(dicionario, arq_json) # O METODO [JSON.DUMP] ==> ELE ADD O QUE TA NO ARQUIVO , DENTRO DO DICIONARIO.

# 3° PASSO
## CRIANDO O ARQUIVO [JSON] ==> E PREENCHENDO ELE --> CHAMANDO A FUNCAO SÓ PRA CRIAR E PREENCHER
def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o CÓD DO PRODUTO : ")] = [
            input("Digite a data da última COMPRA : "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()

        # APÓS PREENCHER O ARQUIVO , EU CHAMO A FUNCAO DE CIMA , PARA APENAS ESCREVER E GUARDAR EM JSON, USANDO O METODO [JSON.DUMP]
        gravar_arquivo(dicionario,arquivo) # REPARE Q AQUI EU ESTOU CHAMANDO A FUNCAO DE PREENCHER E GRAVAR O ARQUIVO COMO JSON

    #obs poderia ser assim tbm ==>
    """     with open(arquivo, "w") as arq_json: # ESCREVENDO NO ARQUIVO 1°
        json.dump(dicionario, arq_json) # O METODO [JSON.DUMP] ==> ELE ADD O QUE TA NO ARQUIVO , DENTRO DO DICIONARIO. """

    return "JSON gerado!!!!"

# 5° passo
## EXIBINDO ARQUIVO == > JSON
def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    cont = 0
    for chave, dado in dicionario.items():
        cont +=1
        print("N° do PRODUTO ....: ", cont)
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2],"\n")

# AGORA Q EU CRIEI AS FUNCOES == > SÓ FAZER A CHAMDA NO ARQUIVO ==> MANIPULA_ARQUIVO_JSON
