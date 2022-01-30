### CRIANDO PROGRAMA ==> PARA CALCULAR FRETE

# IMPORTAR AS BIBLIOTECAS COM O PIP...

## VIDEO DO APP ==> https://www.youtube.com/watch?v=0CX1CN8rPrg&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=12
from PyQt5 import uic, QtWidgets

from PyQt5.QtWidgets import QMessageBox   ## isso aqui permite mandar mensagem pro usuario na caixa de box

import mysql.connector

from reportlab.pdfgen import canvas

banco = mysql.connector.connect(  # CRIANDO OBJETO BANCO > E USANDO O METODO > MYSQ... PRA CHAMAR O BANCO
    host="localhost",
    user="root",
    password="###",
    database="calcFrete"
)


# ============ ++ ========================================

# CRIANDO UM APP QUE CALCULA FRETE > OBS > AS TELAS EU CRIEI NO (QT DESIGNER) > CRIEI O BANCO (CALCfRETE) E PUXEI OS DADOS DO BANCO NAS MINHAS [COMBOX]

# OBS 2 > LA EMBAIXO VC FAZ AS CHAMADAS > E AQUI ENCIMA VC FAZ AS FUNÇÕES


## CRIANDO FUNÇÃO > PRA QUANDO CLICAR EM CALCULAR FRETE > MOSTRAR O RESULTADO Q EU QUERO

def consultarContatos():
    tela.show()  # USANDO ISSO PARA ABRIR O LISTA_CONTATOS UI metodo pra mostrar  os contatos > LA EMBAIXO EU DEFINI TUDO

    # PEGANDO O VALOR DOS INPUTS > PREÇO /  PESO / ICMS

    preco = float(tela.lineEdit.text())
    print("Preço (R$): ", preco)
    peso = float(tela.lineEdit_2.text())
    print("Peso (KG): ", peso)
    icms = float(tela.lineEdit_3.text())
    print("Icms (%): ", icms)

    porc = icms / 100

    pedagio = 4.20  # valor padrao conforme a tabela
    print("Pedágio (R$): ",pedagio)


    comb1 = tela.comboBox.currentText(); # esse currentText() -> pega o valor q foi selecionado dentro do [comboBox]

    comb2 = tela.comboBox_2.currentText();

    comb3 = tela.comboBox_3.currentText();

    comb4 = tela.comboBox_4.currentText();

    comb5 = tela.comboBox_5.currentText();

    comb6 = tela.comboBox_6.currentText();


    # pela atividade q o prof propros > o calculo do ==> frete total = pedagio + Valorpeso(capital/interior) + valor_prod + peso ]
    # apos descobrir quanto sai o valor final > eu preciso fazer uma conta se vale  a pena ou nao o frete e entao exibi-lo na tela

    # formula da incidencia > [valor da entrega / valor da mercadoria ] ==> se for maior q 2% do valor do prod nao vale  apena


    # FAZENDO AS VALIDAÇÕES dos combobox
    ## obs==> tem como fazer de maneira mais facil, porem vou usar o IF E ELSE MESMO..

    if (comb1 == "ES" and comb2 == "CAPITAL" and comb3 == "VITORIA" and comb4 == "ES" and comb5 =="CAPITAL" and comb6=="VITORIA"
    or comb1 == "ES" and comb2 == "CAPITAL" and comb3 == "VITORIA" and comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"
    or comb1 == "ES" and comb2 == "INTERIOR" and comb3 == "SERRA" and comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"
    or comb1 == "ES" and comb2=="INTERIOR" and comb3 == "SERRA" and comb4 == "ES" and comb5 == "CAPITAL" and comb6 == "VITORIA"
    or comb1 == "ES" and comb2 == "INTERIOR" and comb3 == "SERRA" and comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"):



        #if(comb4 == "ES" and comb5=="CAPITAL" and comb6 == "VITORIA" or comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"):

        try:

                    ## IMPORTANTE > O QUE DEVEMOS LEVAR EM CONTA É PRA ONDE ELE VAI > SE É CAPITAL OU INTERIOR
            if (peso <= 10.0 and comb5 == "CAPITAL"):
                valorPeso = 16.22
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if(incidencia < 2):
                    tela.label_13.setText(f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')

                return ## obs > o RETURN > SERVE PRA NAO CONTINUAR O PROGRAMA > NO CASO ELE CHEGA NESSA PARTE E PARA AQUI > ELE NAO CONTINUA VERIFICANDO > ISSO EVITA DE FECHAR O PROGRAMA AUTOMATICO


            elif (peso <= 10.0 and comb5 == "INTERIOR"):
                valorPeso = 17.95
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')

                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 10.0 and peso <= 20.0 and  comb5 == "CAPITAL"):

                valorPeso = 24.00
                frete =pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 10.0 and peso <= 20.0 and comb5 == "INTERIOR"):

                valorPeso = 18.50
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return
            elif (peso > 20 and comb5 == "CAPITAL"):

                valorPeso = (peso-20)*0.26 + 24.00
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 20 and comb5 == "INTERIOR"):

                valorPeso = (peso-20)*0.20 + 18.50
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete  é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):

                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return
        except:

            QMessageBox.about(tela, "alerta", "O peso não está correspondendo")



    ## AGORA VOU FAZER UMA 2° VALIDAÇÃO > A 1° SÓ VALIDEI O ESTADO DE (ES)

    ## FAZENDO COMPARAÇÃO DE ES COM SP

    elif (comb1 == "ES" and comb2 == "CAPITAL" and comb3 == "VITORIA" and comb4 == "SP" and comb5 == "CAPITAL" and comb6 == "SÃO PAULO"
    or comb1 == "ES" and comb2 == "CAPITAL" and comb3 == "VITORIA" and comb4 == "SP" and comb5 == "INTERIOR" and comb6 == "SOROCABA"
    or comb1 == "ES" and comb2 == "INTERIOR" and comb3 == "SERRA" and comb4 == "SP" and comb5 == "CAPITAL" and comb6 == "SÃO PAULO"
    or comb1 == "ES" and comb2 == "INTERIOR" and comb3 == "SERRA" and comb4 == "SP" and comb5 == "INTERIOR" and comb6 == "SOROCABA"
    or comb1 == "SP" and comb2 == "CAPITAL" and comb3 == "SÃO PAULO" and comb4 == "ES" and comb5 == "CAPITAL" and comb6 == "VITORIA"
    or comb1 == "SP" and comb2 == "CAPITAL" and comb3 == "SÃO PAULO" and comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"
    or comb1 == "SP" and comb2 == "INTERIOR" and comb3 == "SOROCABA" and comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"
    or comb1 == "SP" and comb2 == "INTERIOR" and comb3 == "SOROCABA" and comb4 == "ES" and comb5 == "CAPITAL" and comb6 == "VITORIA"):



        # if(comb4 == "SP" and comb5 == "CAPITAL" and comb6 == "SÃO PAULO" or comb4 == "SP" and comb5 == "INTERIOR" and comb6 == "SOROCABA"
        # or comb4 == "ES" and comb5 == "CAPITAL" and comb6 == "VITORIA" or comb4 == "ES" and comb5 == "INTERIOR" and comb6 == "SERRA"):

        try:

                    ## IMPORTANTE > O QUE DEVEMOS LEVAR EM CONTA É PRA ONDE ELE VAI > SE É CAPITAL OU INTERIOR
            if (peso <= 10.0 and comb5 == "CAPITAL"):
                valorPeso = 10.00
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco

                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso <= 10.0 and comb5 == "INTERIOR"):
                valorPeso = 13.00
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 10.0 and peso <= 20.0 and  comb5 == "CAPITAL"):

                valorPeso = 14.80
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 10.0 and peso <= 20.0 and comb5 == "INTERIOR"):

                valorPeso = 19.24
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return
            elif (peso > 20 and comb5 == "CAPITAL"):

                valorPeso = (peso-20)*0.16 + 14.80
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return

            elif (peso > 20 and comb5 == "INTERIOR"):

                valorPeso = (peso-20)*0.21 + 19.24
                frete = pedagio + valorPeso + (preco / (1 - porc))
                tela.label_7.setText(f'O Valor total do frete  é (peso+mercadoria+icms+pedagio) = : R$ {frete:.2f} ')
                incidencia = frete / preco
                if (incidencia < 2):
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE VALE A PENA')
                else:
                    tela.label_13.setText(
                        f'O valor da incidência sobre este frete é (%): {incidencia:.2f} FRETE NÃO VALE A PENA')
                return
        except:

            QMessageBox.about(tela, "alerta", "O peso não está correspondendo")

    else:

        QMessageBox.about(tela, "alerta", "A Uf / Cidade Não são correspondentes, verifique novamente")
        return ## obs > o RETURN > SERVE PRA NAO CONTINUAR O PROGRAMA > NO CASO ELE CHEGA NESSA PARTE E PARA AQUI > ELE NAO CONTINUA VERIFICANDO > ISSO EVITA DE FECHAR O PROGRAMA AUTOMATICO


        ## calculando o valor da mercadoria + o icms = frete

    tela.label_7.setText(f'O Valor total do frete é (peso+mercadoria+icms) = : R$ {frete:.2f} ')


# AQUI É ONDE EU FAÇO TODAS AS CHAMADAS DAS FUNÇÕES LA ENCIMA... > FAÇO A CHAMADA DAS TELAS E TBM DOS BOTÕES...

app = QtWidgets.QApplication([])  # AQUI EU CHAMO O PROGRAMA QT

tela = uic.loadUi("calc.ui") # carrego a pagina inicial
tela.show()  # mostro a pagina

tela.btnConsulta.clicked.connect(consultarContatos)  # faço um evento no botão e dou o nome da minha funcao pra ele


## AGORA EU VOU COLOCAR OS DADOS DENTRO DAS MINHAS [COMBOX] EXISTE DUAS MANEIRAS > 1 ° FAZER TUDO NA UNHA MANUAL, OU PUXAR DO BANCO , NO CASO EU VOU PUXAR DO BANCO

# PUXANDO OS DADOS PARA SEREM EXIBIDOS DO BANCO > NA MINHA TABELA DE REFERENCIA

# 1° EXIBINDO OS DADOS DA TABELA DE REFERENCIA PRINCIPAL
cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
comando_SQL = "select uf_peso,regiao_peso,ate_10_kg,ate_20_kg,kg_excedente,pedagio,vigencia from tbl_pesoUf;"  # USANDO O COMANDO SQL
cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

tela.tabelaContatos.setRowCount(
    len(contatosLidos))  # AQUI ELE VAI PEGAR TODAS AS LINHAS LIDAS e vai setar no qt
tela.tabelaContatos.setColumnCount(7)  # AQUI SÓ VAI PEGAR 5 COLUNAS e vai setar nas colunas

for i in range(0, len(contatosLidos)):  # AQUI VAI LER TODOS OS CONTATOS > aqui vai ser as linhas
    for f in range(0, 7):  # E VAI SELECIONAR DO 1° ATÉ O T° > aqui vai ser as colunas
        tela.tabelaContatos.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][
                                                                             f])))


## 2° COLOCANDO AS (UFS - INICIO / FIM ) NO COMBOX PUXANDO DO BANCO DE DADOS

# UF (INICIO) = PARTIDA
cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
comando_SQL = "select uf from tbl_uf;"  # USANDO O COMANDO SQL
cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

for i in range(0, len(contatosLidos)):
    tela.comboBox.addItems([str(contatosLidos[i][0])])  ## o for vai pegar cada linha e vai guardar no (I) e o [0] SIGNIFICA A COLUNA Q EU QUERO > no caso a 1°
#tela.comboBox.addItem(str(contatosLidos[0][0]))

## UF (FIM) = CHEGADA

cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
comando_SQL = "select uf from tbl_uf;"  # USANDO O COMANDO SQL
cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

for i in range(0, len(contatosLidos)):
    tela.comboBox_4.addItems([str(contatosLidos[i][0])])  ## o for vai pegar cada linha e vai guardar no (I) e o [0] SIGNIFICA A COLUNA Q EU QUERO > no caso a 1°
#tela.comboBox.addItem(str(contatosLidos[0][0]))

# ===================== ++ ========================== +++= ===========================

## ADD REGIÃO (INICIO / FIM) # oBS > ESSE VOU TENQ ADD NA MÃO > AO INVÉS DE PUXAR DO BANCO > PQ TEM UM MONTE DE DADOS REPETIDOS > (CAPITAL E INTERIOR)
# O CERTO SERIA EU QUERIA UMA TBL SIMPLES > REGIAO > E COLOCAR SÓ CAPITAL E INTERIOR , AI EU PUXAVA AQUI , MAS N QUERO FAZER ENTAO VOU FAZER NA MAO MESMO



# INICIO
tela.comboBox_2.addItems(["CAPITAL","INTERIOR"])

# FIM
tela.comboBox_5.addItems(["CAPITAL","INTERIOR"])

### ===================== +++ ====================== +++===================================

## ADD TODAS AS CIDADES AGORA DO BANCO DA TBL_ CIDADES

## ADD CIDADES (INICIO)

cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
comando_SQL = "select cidade from tbl_cidades;"  # USANDO O COMANDO SQL
cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

for i in range(0, len(contatosLidos)):
    tela.comboBox_3.addItems([str(contatosLidos[i][0])])

## ADD CIDADES (FIM)

cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
comando_SQL = "select cidade from tbl_cidades;"  # USANDO O COMANDO SQL
cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

for i in range(0, len(contatosLidos)):
    tela.comboBox_6.addItems([str(contatosLidos[i][0])])

## PRONTO AGORA Q EU JA INSERIR OS DADOS DO BANCO > NAS MINHAS [COMBOX] EU APENAS VOU FINALIZAR O QUE QUERO NA FUNÇÃO DO BOTÃO CALCULAR


# FECHANDO O BANCO PRA NAO FICAR ABERTO..
banco.close()
app.exec()  ## EXECUTANDO O APP

