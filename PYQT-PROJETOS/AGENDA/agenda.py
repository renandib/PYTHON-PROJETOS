## CRIANDO PROGRAMA AGENDA NO PYQT5
## não pode esquecer de baixar essas bibliotecas com o PIP..

## VIDEO DO PROGRAMA ==>  https://www.youtube.com/watch?v=rufyL_fF2W8&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=11&t=142s

from PyQt5 import uic, QtWidgets

import mysql.connector

from reportlab.pdfgen import canvas

banco = mysql.connector.connect(  # CRIANDO OBJETO BANCO > E USANDO O METODO > MYSQ... PRA CHAMAR O BANCO
    host="localhost",
    user="root",
    password="###",
    database="agenda"
)


# ============ ++ ========================================


def main():  # CRIANDO UMA FUNÇÃO PRO BOTAO CADASTRAR  > funcao principal

    # AQUI EU TO PEGANDO TODOS OS CAMPOS DA MINHA TELA ATRAVES DO METODO > TELA.NOMEDOCOMPONENTE.TEXT()
    campoId = agenda.leId.text()
    print("OK: ", campoId)
    campoNome = agenda.leNome.text()
    print("Nome: ", campoNome)
    campoEmail = agenda.leEmail.text()
    print("Email: ", campoEmail)
    campoTelefone = agenda.leTelefone.text()
    print("Telefone: ", campoTelefone)

    tipoTelefone = ""

    if agenda.rbResidencial.isChecked():  # AQUI EU TO TESTANDO O RADIOBUTTON ATRAVES DO METODO > ISCHECKED()
        print("Tipo de telefone é Residencial")
        tipoTelefone = "Residencial"

    elif agenda.rbCelular.isChecked():
        print("Tipo de telefone é Celular ")
        tipoTelefone = "Celular"

    else:
        print("Informe o tipo do telefone !")
        tipoTelefone = "Não informado"

        # AGORA VOU INSERIR OS DADOS NO BANCO > LA ENCIMA EU JA CHAMEI O BANCO

    cursor = banco.cursor()  # ESSE METODO > CURSOR Q PERMITE ISSO
    comando_SQL = 'INSERT INTO contatos (nome,email,telefone,tipoTelefone) VALUES (%s,%s,%s,%s);'  # USANDO O COMANDO PRA ADD NO BANCO
    dados = (str(campoNome), str(campoEmail), str(campoTelefone),
             tipoTelefone)  # CRIANDO UM OBJETO PRA PEGAR TODOS OS CAMPOS DA TELA
    cursor.execute(comando_SQL,
                   dados)  # USANDO O COMANDO > CURSOR.EXECUTE > PRA PEGAR O CODIGO SQL + OS DADOS Q EU TENHO
    banco.commit()  # COMITANDO > PASSANDO A LIMPO PRO BANCO

    # DPS DE CLICAR EM CADASTRAR > PRA FICAR LIMPO NOVAMENTE OS CAMPOS PRA UM NOVO PREENCHIMENTO EU FAÇO ISSO
    agenda.leId.setText("")
    agenda.leNome.setText("")
    agenda.leEmail.setText("")
    agenda.leTelefone.setText("")

    # AGORA VOU CRIAR A FUNCAO PRO BOTAO CONSULTAR > QUANDO CLICAR NELE VAI LEVAR PRA OUTRA TELA > E VAI APARECER TUDO Q EU JA TENHO CADASTRADO


def consultarContatos():
    listarContatos.show()  # USANDO ISSO PARA ABRIR O LISTA_CONTATOS UI metodo pra mostrar  os contatos > LA EMBAIXO EU DEFINI TUDO

    cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
    comando_SQL = "SELECT * FROM contatos"  # USANDO O COMANDO SQL
    cursor.execute(comando_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
    contatosLidos = cursor.fetchall()  # ESSE METODO > VAI BUSCAR LINHA POR LINHA do banco

    listarContatos.tabelaContatos.setRowCount(
        len(contatosLidos))  # AQUI ELE VAI PEGAR TODAS AS LINHAS LIDAS e vai setar no qt
    listarContatos.tabelaContatos.setColumnCount(5)  # AQUI SÓ VAI PEGAR 5 COLUNAS e vai setar nas colunas

    for i in range(0, len(contatosLidos)):  # AQUI VAI LER TODOS OS CONTATOS > aqui vai ser as linhas
        for f in range(0, 5):  # E VAI SELECIONAR DO 1° ATÉ O T° > aqui vai ser as colunas
            listarContatos.tabelaContatos.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][
                                                                                           f])))  # AQUI VAI PEGAR TODOS OS ITENS E VAI SETAR NUM LUGAR SÓ > Q É NA TELA > LISTACONTATOS


# AGORA JA FOI O CADASTRAR E O CONSULTAR CONTATOS > AGORA FALTA FAZER A FUNÇÃO > EXCLUIR CONTATOS >E GERAR PDF

def excluirContato():
    linhaContato = listarContatos.tabelaContatos.currentRow()  # OBS NO SLIDE DA PROF TA SEM PONTO ANTES DO CURRENT.. > currentrow() SIGNIFICA > ( LINHA ATUAL ) # > aqui ele pega a linha q eu selecionar
    listarContatos.tabelaContatos.removeRow(linhaContato)  # aqui ele vai remover a linha atual q eu selecionei

    cursor = banco.cursor()  # CHAMANDO O BANCO
    comando_SQL = "SELECT id FROM contatos"  # SELECIONAR POR ID > DO ELEMENTO Q EU ESCOLHI
    cursor.execute(comando_SQL)  # aqui só ta fazendo executar a linha de cima
    contatos_lidos = cursor.fetchall()  # pega linha por linha no banco
    valorId = contatos_lidos[linhaContato][0]
    cursor.execute("DELETE FROM contatos WHERE id=" + str(valorId))
    banco.commit()


# AGORA Q EU JA FIZ > CADASTRAR / CONSULTAR / EXCLUIR CONTATO > VOU FAZER GERAR PDF > E DPS VOU FAZER A TELA ALTERAR CONTATO..


def voltar():
    listarContatos.close()  # > AQUI ELE VAI FECHAR A TELA > LISTA CONTATOS > Q EU ABRI LA EMBAIXO A CHAMADA > DA TELA E TBM FIZ MAIS EMBAIXO  A MUDANÇA DO BOTAO VOLTAR
    agenda.close()  # > O CERTO É DEIXAR ISSO AQUI > PQ ELE IA FECHAR A 1° TELA Q JA TAVA ABERTA E DPS IA ABRI-LA
    agenda.show()  # > rapidamente ele vai fechar e abrir AQUI > quando eu mostrar pelo metodo show
    print("Deu certo")


def fechar():
    altera.close()


def alterar():
    # altera.show()
    # campoNome = altera.leNome.text()
    # campoEmail = altera.leEmail.text()
    # campoTelefone = altera.leTelefone.text()

    linhaContato = listarContatos.tabelaContatos.currentRow()

    campoNome = listarContatos.leNome.text()
    campoEmail = listarContatos.leEmail.text()
    campoTelefone = listarContatos.leTelefone.text()

    cursor = banco.cursor()  # CHAMANDO O BANCO
    comando_SQL = "SELECT id FROM contatos"  # SELECIONAR POR ID > DO ELEMENTO Q EU ESCOLHI
    cursor.execute(comando_SQL)  # aqui só ta fazendo executar a linha de cima
    contatos_lidos = cursor.fetchall()  # pega linha por linha no banco
    valorId = contatos_lidos[linhaContato][0]

    cursor = banco.cursor()  # USANDO O METODO CURSOR > PRA ACESSAR O BANCO
    comandos_SQL = "UPDATE contatos SET nome='" + campoNome + "',email='" + campoEmail + "',telefone='" + campoTelefone + "' WHERE id=" + str(
        valorId)
    # comandos_SQL = "UPDATE contatos SET nome='FODAO',email='FODAO@GMAIL.COM',telefone='555' WHERE id="+str (valorId)  # > ISSO AQUI DA CERTO > PQ O DE CIMA NAO..

    cursor.execute(comandos_SQL)  # USANDO O METODO EXECUTE > PRA FUNCIONAR O SQL
    listarContatos.tabelaContatos.setRowCount(len(comandos_SQL))
    banco.commit()

    listarContatos.leNome.setText("")
    listarContatos.leEmail.setText("")
    listarContatos.leTelefone.setText("")


def gerarPdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "lista de contatos")

    pdf.setFont("Times-Bold", 14)  # aqui COMANDA OS TITULOS > 1° n é a margem > 2° é a altura
    pdf.drawString(10, 750, "ID")
    pdf.drawString(70, 750, "NOME")
    pdf.drawString(210, 750, "EMAIL")
    pdf.drawString(410, 750, "TELEFONE")
    pdf.drawString(510, 750, "TIPO")

    for i in range(0, len(contatos_lidos)):  # ISSO AQUI COMANDO OS DADOS > N° ESQUERDA É A MARGEM > 2° N É A ALTURA
        y = y + 50
        pdf.drawString(10, 750 - y, str(contatos_lidos[i][0]))
        pdf.drawString(40, 750 - y, str(contatos_lidos[i][1]))
        pdf.drawString(170, 750 - y, str(contatos_lidos[i][2]))
        pdf.drawString(410, 750 - y, str(contatos_lidos[i][3]))
        pdf.drawString(510, 750 - y, str(contatos_lidos[i][4]))

    pdf.save()
    print("PDF SALVO COM SUCESSO!")  # OBS <> O PDF É SALVO NA MESMA PASTA DAS TELAS..


# AQUI É ONDE EU FAÇO TODAS AS CHAMADAS DAS FUNÇÕES LA ENCIMA... > FAÇO A CHAMADA DAS TELAS E TBM DOS BOTÕES...

app = QtWidgets.QApplication([])  # AQUI EU CHAMO O PROGRAMA QT
agenda = uic.loadUi("agenda.ui")  # AQUI EU CARREGO A PAGINA AGENDA
listarContatos = uic.loadUi("listaContatos.ui")  # AQUI EU CARREGO A PAGINA LISTACONTATOS
altera = uic.loadUi("alterarContato.ui")
altera.btnConfirmar.clicked.connect(fechar)
agenda.btnCadastro.clicked.connect(main)  # AQUI EU FAÇO O METODO CLICKED > QUANDO CLICAR ELE EXECUTA A FUNCAO MAIN
agenda.btnConsulta.clicked.connect(
    consultarContatos)  # AQUI O OUTRO CLICKED > VAI EXECUTAR A OUTRA FUNCAO > CONSULTARCONTATOS
listarContatos.btnVoltar.clicked.connect(voltar)
listarContatos.btnAlterar.clicked.connect(alterar)

listarContatos.btnExcluirContato.clicked.connect(
    excluirContato)  # aqui eu to fazendo o clicked > fazer a funcao > excluir contato > na tela listacontatos
listarContatos.btnGerarPdf.clicked.connect(
    gerarPdf)  # aqui eu to fazendo o clicked > fazer a funcao > gerarpdf > na tela listacontatos

agenda.show()

app.exec()
