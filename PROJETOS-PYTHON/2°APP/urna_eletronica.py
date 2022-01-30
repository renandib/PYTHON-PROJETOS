#Desenvolver código Python para uma urna eletrônica com pelo menos 3 candidatos, a opção de voto em branco e com reconhecimento de voto nulo (para qualquer entrada não prevista).
#O programa deverá ser iniciado requisitando senha para início dos trabalhos.
#Em seguida, deverão ser apresentados códigos de cada um dos candidatos e a opção de voto em branco.
#Após cada voto ser computado, deverá ser oferecida opção para “liberar para novo voto” ou o "encerramento do processo de eleição". Cada nova ação, seja novo voto ou seja encerramento, deverá ser liberada pela validação da senha.
#Ao término do processo o programa deverá indicar as porcentagens totais (considerando todo o universo de votos), as porcentagens dos votos válidos (desconsiderando nulos e brancos) e os valores absolutos para cada candidato.
#Também, informar o eleito.

###======>>> URNA ELEITORAL

## VIDEO DO APP ==> https://www.youtube.com/watch?v=5gWEgYHAKZU&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=3

## OBS ==> TEM COMO FAZER USANDO FUNÇÕES E TAMBEM UTILIZANDO MANEIRAS MAIS TRANQUILAS , POREM PREFERI FAZER ASSIM PARA TREINO

resp=0  # fazendo uma resposta para parar o looping
cont=0 # esses são os votos totais > A cada volta vai gerar um contador >> vai ser o contador total de votos
nulo=0  # criando os votos nulos
branco=0 # criando os brancos
cand1=0  # n° de votos individuais do
cand2=0
cand3=0
venc=""
validos=0

while True:

    senha=int(input("\n**  Mesário, digite a senha para dar um novo acesso de voto ao eleitor ** "))
    if(senha!=123):
        print(" ** Senha incorreta, digite novamente ! ")
    else:

        print("  \n ================= >  CANDIDATOS : [10] LULA  /  [11] BOLSONARO / [12] DATENA  < ==================== \n")
        num = int(input(" => => Para votar em um [CANDIDATO]. Digite um n° [].  Se quiser VOTAR EM BRANCO = [1] / NULO = [diferente] "))
        conf= int(input(" **  Deseja confirmar seu voto Digite [2]. Caso contrario [ 3 ] para voltar."))
        cont += 1


        if(num==10 and conf==2):
            cand1+=1
            print(" **  Voto Confirmado!  **")

        elif(num==11 and conf==2):
            cand2+=1
            print(" **  Voto Confirmado!  **")
        elif(num==12 and conf==2):
            cand3+=1
            print(" **  Voto Confirmado!  **")

        elif(num==1 and conf==2):
            branco+=1
            print(" **  Voto confirmado!  **")

        elif(num==10 and conf==3):
            cand1+=0
            cont-=1
            print(" *** Seu voto não foi confirmado. Volte a escolher um novo candidato e confirme seu voto!  ***")

        elif(num==11 and conf==3):
            cand2+=0
            cont-=1
            print(" *** Seu voto não foi confirmado. Volte a escolher um novo candidato e confirme seu voto!  ***")

        elif(num==12 and conf==3):
            cand3+=0
            cont-=1
            print(" *** Seu voto não foi confirmado. Volte a escolher um novo candidato e confirme seu voto!  ***")

        elif(num==1 and conf==3):
            branco+=0
            cont-=1
            print(" *** Seu voto não foi confirmado. Volte a escolher um novo candidato e confirme seu voto!  ***")


        else:
            if(conf==2):
                nulo += 1
                print(" **  Voto confirmado!  **")
            elif(conf==3):
                nulo += 0
                cont-=1
                print(" *** Seu voto não foi confirmado. Volte a escolher um novo candidato e confirme seu voto!  ***")

        resp = int(input("===>> DESEJA SAIR DA VOTAÇÃO ? DIGITE > [0]. CASO CONTRARIO DIGITE QUALQUER N° "))
        print("=====  *** ===== *** ====== **** ")
        if(resp==0):
            validos=cont-(branco+nulo)
            porc1=(cand1*100)/validos
            porc2=(cand2*100)/validos
            porc3=(cand3*100)/validos
            porc4=(branco*100)/cont+1
            porc5=(nulo*100)/cont+1
            if(porc1>porc2 and porc1>porc3):
                venc = "LULA"
            elif(porc2>porc1 and porc2>porc3):
                venc = "BOLSONARO"
            elif(porc3>porc1 and porc3>porc2):
                venc = "DATENA"
            else:
                print("Sem ganhador!")
            break


print(f'--- \n O N° TOTAL DE VOTOS FOI : [ {cont} ]. [BRANCOS] = [ {branco} ] / [NULOS] = [ {nulo} ]')
print(f'--- \n OS VOTOS VALIDOS FORAM : [ {validos} ]. A PORCENTAGEM EM RELAÇÃO AOS VOTOS VALIDOS DE CADA CANDIDATO É > [LULA] = [ {(cand1*100)/validos:.2f} % ] / [BOLSONARO] = [ {(cand2*100)/validos:.2f} % ] / [DATENA] = [ {(cand3*100)/validos:.2f} % ] ')
print(f'--- \n A PORCENTAGEM DE VOTOS DE CADA CANDIDATO EM RELAÇÃO AO N° TOTAL DE VOTOS É : [LULA] = [{(cand1*100)/cont:.2f} % ] / [BOLSONARO] = [ {(cand2*100/cont):.2f} % ] / [DATENA] = [ {(cand3*100/cont):.2f} % ] ')
print(f'--- \n O N° DE VOTOS INDIVIDUAIS FORAM : [LULA] = [{cand1}] / [BOLSONARO] = [{cand2}] / [DATENA] = [{cand3}]')
print(f'--- \n O MAIOR  N° DE VOTOS FOI DO : [{venc}]. PORTANTO ELE FOI O CANDIDATO ELEITO ! ')





