nota1, nota2 = float(input('Digite nota 1: ')), float(input('Digite nota 2: '))
print('Reprovado' if((nota1 + nota2) /2) < 7 else 'Aprovado com distinção' if((nota1 + nota2)/2) == 10 else 'Aprovado') 