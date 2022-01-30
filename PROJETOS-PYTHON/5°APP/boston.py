# 4° )
##### MANIPULANDO ARQUIVOS DE TERCEIROS

##==> VIDEO DO APP ==> https://www.youtube.com/watch?v=OGfBhndZ7Ws&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=8

##=>  BAIXAR O ARQUIVO ==> ECONOMIC-INDICATORS ==> É UM ARQUIVO Q CONTEM ALGUNS DADOS E CHAVES

# aqui eu explico o que eu quero fazer com esse arquivo

# 1) pegar o total de voos internacionais que partiram do aeroporto de logan no ano de 2014 ?
# 2) Quando (mes/ano) ocorreu o maior transito de passageiros no aeroporto de logan?
# 3) Qual o total de passageiros que passaram pelo aeroporto de logan, no ano que for especificado pelo usuario ?
# 4) Qual o mês que possui a maior média da diaria de um hotel , com base no ano especificado pelo usuario ?

## ANTES DE FAZER ISSO É BOM SABER ALGUNS TERMOS DO ARQUIVO ==> CHAVES

# YEAR = ano / MONTH = mes / LOGAN_PASSAGERS = qnt de passaeiros de logan / LOGAN_INTL-FLIGTHS = voos internacionais q partiram de logan

# HOTEL_OCCUP_RATE = Porcentagem de vagas ocupadas nos hoteis de boston

# HOTEL_AVG_DAILY_RATE = média da diaria em dolar de um hotel em boston

#total_jobs , unemp_rate = porcentagem de desempregados em bosto


###### RESPONDENDO AS PERGUNTAS

# PARA FICAR MELHOR O COD => OLHA O ARQUIVO ==> ECONOMIC....CSV = > E REPARE ONDE FICA AS COISAS.. AI FICA MELHOR PRA FAZER O COD

with open("economic-indicators (1).csv","r") as boston:
    total_voos=0
    maior=0
    total_passageiros=0
    maior_media_diaria=0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    for linha in boston.readlines()[1:-1]:  # LEMBRANDO Q [0] É O TITULO => ENTAO PARA LER OS DADOS COMEÇA DE [1:-1] ATÉ O FINAL PRA LER TUDO
        lista=linha.split(",")   # IDENTIFICOU O QUE SEPARA TUDO
        total_voos += float(lista[3])  # [3] É A COLUNA DE VOOS INTERNACIONAS Q PARTIRAM DE LOGAN  => 1° TRANSFORMA EM FLOAT DPS SOMA TUDO COM O += AI VAI TER O TOTAL ==> JA É A RESPOSTA DA 1°

        # RESPOSTA DA 2° ==> MES/ANO DE MAIOR MOVIMENTO NO AEROPORTO DE LOGAN
        # COMO ISSO ESTA DENTRO DE UM FOR ==> ELE VAI FICAR RODANDO ATÉ O FINAL ==> ENTAO MEU IF==> ELE VAI PRIMEIRO TRANSFORMAR EM FLOAT , PRA DPS ACHAR O ULTIMO VALOR MAIOR
        if float(lista[2])>float(maior): # CONCERTEZA O ULTIMO VALOR VAI SER MAIOR Q 0 ENTAO ==> ELE VAI SABER QUE O MAIOR N DE PASSAGEIROS É TAL..
            maior=lista[2] # AQUI VAI TRANSFORMAR O MAIOR MOVIMENTO DE PASSAGEIROS NO AEROPORTO DE LOGAN
            ano=lista[0] # AQUI TBM VAI PEGAR O MAIOR ANO ==> POR CAUSA DO FOR
            mes=lista[1] # CONS. AQUI TBM VAI PEGAR O MAIOR MES ==> POR CAUSA DO FOR TBM

        # RESPOSTA DA 3° ==> Qual o total de passageiros que passaram pelo aeroporto de logan, no ano que for especificado pelo usuario ?
        if ano_usuario==lista[0]: # VAI COMPARAR SE O ANO Q O USUARIO DIGITOU TEM DENTRO DA TABELA

            total_passageiros += float(lista[2]) # VAI SOMAR TODOS OS VALORES A CADA INTERAÇÃO E NO FINAL TEM O TOTAL DE PASSAGEIROS Q PASSARAM PELO AEROPORTO DE LOGAN

            # RESPOSTA DA 4° ==> 4) Qual o mês que possui a maior média da diaria de um hotel , com base no ano especificado pelo usuario ?

            # REPARE Q AQUI TA DENTRO DO OUTRO IF ==> PQ JA APROVEITA A PRIMEIRA CONDICAO
            if float(lista[5])>float(maior_media_diaria): # 2° COND ==> COMO ESTA DENTRO DE UM FOR LA ENCIMA == > ELE SEMPRE VAI PEGAR O ULTIMO VALOR(MAIOR) => Q CONCERTEZA É MAIOR Q ZERO
                maior_media_diaria=lista[5]  # PEGANDO O VALOR DA MAIOR MÉDIA DE DIARIA DE UM HOTEL

                mes_maior_diaria=lista[1] # APOS ISSO É SÓ PEGAR O MES QUE CORRESPONDE A MAIOR MÉDIA

    ## AGORA IMPRIMO O RESULTADO DE TUDO NOS PRINTS
    print("O total de voos é: ", total_voos)
    print("O mês/ano de maior movimento no aeroporto foi: ",str(mes),"/",str(ano))
    print("O total de passageiros do ano ", ano_usuario,"foi de ", total_passageiros)
    print("O mês do ano ", ano_usuario,"com maior média para diária de hotel foi ", mes_maior_diaria)



