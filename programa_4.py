num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = int(input("1 - adição | 2 - subtração | 3 - multiplicação | 4 - divisão ? "))

if operacao == 1:
	resultado = num1 + num2
	if resultado % 2 == 0:
		print("O numero %d é Par!" % resultado)
	else:
		print("O numero %d é Impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é Negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é Inteiro!" % resultado)
	else:
		print("O numero %.1f é Decimal." % resultado)

if operacao == 2:
	resultado = num1 - num2
	if resultado % 2 == 0:
		print("O numero %d é Par!" % resultado)
	else:
		print("O numero %d é Impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é Negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é Inteiro!" % resultado)
	else:
		print("O numero %.1f é Decimal." % resultado)

if operacao == 3:
	resultado = num1 * num2
	if resultado % 2 == 0:
		print("O numero %d é Par!" % resultado)
	else:
		print("O numero %d é Impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é Negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é Inteiro!" % resultado)
	else:
		print("O numero %.1f é Decimal." % resultado)

if operacao == 4:
	resultado = num1 / num2
	if resultado % 2 == 0:
		print("O numero %d é Par!" % resultado)
	else:
		print("O numero %d é Impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é Negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é Inteiro!" % resultado)
	else:
		print("O numero %.1f é Decimal." % resultado)