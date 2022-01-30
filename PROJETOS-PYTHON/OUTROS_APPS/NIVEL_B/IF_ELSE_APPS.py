## CALCULE O IMC UTILIZANDO IF E ELSE

peso =float(input("Digite seu peso em kg : "))

altura = float(input("Digite sua altura em (M) : "))

conta =peso/(altura*altura)

print(f' Seu peso é de: [{peso} kg ].  A Sua altura é de: [{altura} m ]. Portanto, seu IMC = [ {conta:.2f} Kg/m² ]')

if(conta>=18 and conta<25):{
        print(f' Seu IMC = [{conta:.2f} kg/m² ]. Portanto, você está com o [ PESO NORMAL ]  em relação á sua altura ! ')
    }

elif(conta>=25 and conta<30):{
    print(f'Seu IMC = [{conta:.2f} kg/m² ]. Portanto, você está com [ SOBREPESO ] em relação á sua altura ! ')
}

elif(conta>=30 and conta<35):{
    print(f'Seu IMC = [{conta:.2f} kg/m² ]. Portanto, você está com [ OBESIDADE GRAU 1 ]  em relação á sua altura !')
}

elif(conta>=35 and conta<40):{
    print(f'Seu IMC = [{conta:.2f} kg/m² ]. Portanto, você está com [ OBESIDADE GRAU 2 ] em relação á sua altura !')
}

else:
    print(f'Seu IMC = [{conta:.2f} kg/m² ]. Portanto, você está com  [ OBESIDADE GRAU 3  OU MÓRBIDA ] em  relação á sua altura ! ')
