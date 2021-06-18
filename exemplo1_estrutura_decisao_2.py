altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))

imc = peso / altura**2

if imc < 18.5:
	print("Classificação: ABAIXO DO PESO, IMC:", imc)
elif 18.5 <= imc <= 24.9:
	print("Classificação: Normal, IMC:", imc)
elif 25.00 <= imc <= 29.9:
	print("Classificação: Sobrepeso, IMC:", imc)
elif 30.0 <= imc <= 39.9:
	print("Classificação: Obesidade 2, IMC:", imc)
else:
	print("Classificação: Obesidade grave, IMC:", imc)
