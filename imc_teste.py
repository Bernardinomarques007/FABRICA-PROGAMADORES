print("| CALCULADORA DE IMC ")



altura = float(input("| Digite a sua altura (por favor, no lugar da vírgula coloque um ponto) : "))
peso   = float(input("| Digite seu peso (por favor no lugar da vírgula coloque um ponto) : "))

calc_alt = altura * altura

imc = peso  / calc_alt

if imc <= 18.5 :
    print("| Magreza ")
elif imc == 18.5 or imc < 25:
    print("| Normal ")
elif imc == 25 or imc < 30:
    print("| Sobrepeso ")
elif imc == 30 or imc < 40:
    print("| Obesidade grau |")
elif  imc < 40:
    print("| Obesidade grave")
else:
    print("| Dados insuficientes para efetuar sua solicitação")
