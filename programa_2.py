nota1, nota2 = float(input('Digite nota 1: ')), float(input('Digite nota 2: '))

media = (nota1 + nota2) / 2

if media >= 10:
  print('Você tirou A')
  print('Media: ', media, 'Você está Aprovado!')
  
elif media <= 9 and media >= 7.5:
  print('Você tirou B')
  print('Media: ', media, 'Você está Aprovado!')

elif media >= 6 and media <= 7.5:
  print('Você tirou C')
  print('Media: ', media, 'Você está Aprovado!')

elif media >= 4 and media <= 6:
  print('Você tirou D')
  print('Media: ', media, 'Você está Aprovado!')

elif media <= 4 and media >= 0:
  print('Você tirou E')
  print('Media: ', media, 'Você foi REPROVADO')