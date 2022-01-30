###LAÇOS DE REPETIÇÕES

# WHILE / FOR

# WHILE ==> SEMPRE QUANDO FOR FAZER ALGO REPETITIVO VC USA O WHILE , AO INVES DE FICAR FAZENDO UM MONTE DE CODIGO TODA HORA

## EX DE WHILE (LEMBRANDO Q O WHILE TENQ TER ALGO Q FINALIZA ELE, SE NAO DA LOOP INFINITO)

### ========>>> PROGRAMA ATENDIMENTO DE EMERGÊNCIA

# VIDEO DO APP ==>  https://www.youtube.com/watch?v=XTPxFH9UeMA&list=PLOqx8yEV2-l2_QbDc4PNKeaOH49etj2ax&index=2


resp = "S"

cont = 0 ## criando contador ==> como se fosse uma senha de usuario
# PRIMEIRO PROBLEMA A SER RESOLVIDO


while resp == "S":
    cont +=1  ## a cada usuario que fizer o registro ==> vai salvar um numero==> de prioridade = SENHA

    print("******** ATENDIMENTO DE EMERGÊNCIA MÉDICA **********\n")
    nome = input("Digite o nome: ")
    print("até 6 anos - criança \n"
          "até 65 anos - adulto \n"
          "65 em diante - idoso \n")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? DIGITE ==> (SIM/NÃO) ").upper()

    # COMPARANDO PESSOAS Q TEM SUSPEITA DA DOENÇA
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA[URGÊNCIA]")

        if idade <= 6:
            genero = input("Digite o gênero do paciente(a): ").upper()
            print("PACIENTE [CRIANÇA] COM PRIODADE [MÁXIMA] ")
        elif idade >= 65:
            genero = input("Digite o gênero do paciente(a): ").upper()
            print("Paciente [IDOSO(A)] COM PRIORIDADE [MÁXIMA]")
        else:
            genero = input("Digite o gênero do paciente(a): ").upper()
            if genero == "FEMININO" and idade > 10:
                gravidez = input("A paciente está grávida? ").upper()
                if gravidez == "SIM":
                    print("Paciente [GRAVIDA] COM prioridade [MÁXIMA]")
                else:
                    print("Paciente [ADULTO-FEMININO] COM PRIORIDADE [MÉDIA] ")
            else:
                print("Paciente [ADULTO-MASCULINO] COM PRIORIDADE [MÉDIA] ")

    # SEGUNDO PROBLEMA A SER RESOLVIDO ==> PESSOAS Q NAO TEM CERTEZA SE TEM.
    else:
        print("Encaminhe o paciente para sala BRANCA [PARA MAIORES DETALHES] ")

        if idade <= 6 :
            genero = input("Digite o gênero do paciente(a): ").upper()
            print("PACIENTE [CRIANÇA] COM PRIODADE [MÁXIMA] ")
        elif idade >= 65:
            genero = input("Digite o gênero do paciente(a): ").upper()
            print("Paciente [IDOSO(A)] COM PRIORIDADE [MÁXIMA]")
        else:
            genero = input("Digite o gênero do paciente(a): ").upper()
            if genero == "FEMININO" and idade > 10:
                gravidez = input("A paciente está grávida? ").upper()
                if gravidez == "SIM":
                    print("Paciente [GRAVIDA] COM prioridade [MÁXIMA]")
                else:
                    print("Paciente [ADULTO-FEMININO] COM PRIORIDADE [MÉDIA] ")
            else:
                print("Paciente [ADULTO-MASCULINO] COM PRIORIDADE [MÉDIA] ")

    print(f'Sua senha é: {cont}')

    resp = input("Digite (S) para continuar: \n").upper()

