#### ====== > PROGRAMA --> PREENCHENDO RELATÓRIOS UTULIZANDO FUNÇÕES E DICIONARIOS

## VIDEO DO APP ==>https://www.youtube.com/watch?v=OCGoMe3Qyoc&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=6

## CRIANDO AS FUNÇÕES PRIMEIRO

# 2°)
# CRIANDO PEQUENO PROGRAMA PARA DEMONSTRAR O PODER DOS DICIONARIOS


# ***** CRIANDO PROGRAMA (JEITO MELHOR) ==> USANDO FUNCOES

from datetime import datetime


def perguntar():
    resposta = input("O que deseja realizar? \n" +
                     "<I> - Para Inserir um usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para Listar um usuário: \n" +
                     "<S> - Para SAIR \n").upper()
    return resposta


# ******** INSERINDO USUARIO
def inserir(dicionario):
    horario = datetime.now()  # funcao q mostra DATA/MES/ANO / H / M / S
    # VOU USAR UMA FUNÇÃO CHAMADA ==> [STRFTIME] ==> CONVERTE A FUNCAO DE HORA EM UMA STRING ==> AONDE EU DECIDO O QUE QUERO Q MOSTRA ==>
    exato = horario.strftime(
        '%d/%m/%y - %H : %M')  ## AQUI EU VOU MOSTRAR DIA / MES / ANO / HORA : MINUTO ==> CONFORME A STRING Q EU MONTEI..

    dicionario[input("Digite o login [CHAVE] : ").upper()] = [input("Digite o nome: ").upper(), (exato),
                                                              input("Qual a última estação acessada: ").upper()]

    # print("USUÁRIO REGISTRADO COM SUCESSO\n",dicionario) # só pra mostrar o que tem dentro do dicionario


# ********** PESQUISANDO USUARIO

## OBS ==> A FUNCAO (GET) PESQUISA A CHAVE

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)  ## esse método pesquisa diretamente Na [CHAVE] do DICIONARIO

    if lista != None:

        print("PESQUISA POR LOGIN : \n")
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])  # quando inseriu
        print("Última estação.: " + lista[2])
        # print("horario da pesquisa... : " + lista[3])
    else:

        print("Login inexistente , por favor digite um  LOGIN válido.\n")


## ********* EXCLUINDO USUARIO

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:

        log = dicionario[chave]  # para guardar o valor antigo , antes de excluir
        del dicionario[chave]
        print(f'Usuario {log} foi eliminado do grupo')

    else:
        print("Login inexistente , por favor digite um  LOGIN válido.\n")


## ********* LISTANDO USUARIO

def listar(dicionario):
    esse = []

    for chave, valor in dicionario.items():  # o metodo items()==> mostra cada item com ==> CHAVE : VALOR == > retorna em formato de LISTA == TUPLA

        tudo = [chave, valor]
        esse += tudo

    print(f' "TODOS OS USUÁRIOS : " Login: [dados] ==>  {esse} ')

    # OBS PODERIA FAZER ASSIM TBM O COD ACIMA : POREM O CERTO É GUARDA O RESULTADO EM UMA VARIAVEL

    """
    for chave, valor in dicionario.items():  # o metodo items()==> mostra cada item com ==> CHAVE : VALOR == > retorna em formato de LISTA == TUPLA

    print(f' {chave} : {valor}')
    """

## AGORA QUE EU CRIEI AS FUNÇÕES , VOU FAZER A CHAMADA DELAS NO ARQUIVO == > PREENCHENDO_RELATORIOS....
