print('=========== PROMOÇÃO ===========\n')
print('Até 5 KG\t\t\t Acima de 5 KG')
print('File Duplo R$ 4,90 por KG\t R$ 5,80 por KG\n')
print('Alcatra R$ 5,90 por Kg\t\t R$ 6,80 por Kg\n')
print('Picanha R$ 6,90 por Kg\t\t R$ 7,80 por Kg\n')
print('1 - File Duplo')
print('2 - Alcatra')
print('3 - Picanha\n')
opcao = input("QUAL O TIPO DE CARNE? \n")

if opcao == '1':
    tipo_carne = 'File Duplo'
    qtdecarne = int(input('QUAL A QUANTIDADE DESEJADA? \n'))
    if qtdecarne > 5:
        valor_compra = qtdecarne * 5.8
    else:
        valor_compra = qtdecarne * 4.9
elif opcao == '2':
    tipo_carne = 'Alcatra'
    qtdecarne = int(input('QUAL A QUANTIDADE DESEJADA? \n'))
    if qtdecarne > 5:
        valor_compra = qtdecarne * 6.8
    else:
        valor_compra = qtdecarne * 5.9
elif opcao == '3':
    tipo_carne = 'Picanha'
    qtdecarne = int(input('QUAL A QUANTIDADE DESEJADA ? \n'))
    if qtdecarne > 5:
        valor_compra = qtdecarne * 7.8
    else:
        valor_compra = qtdecarne * 6.9
else:
    print('OPÇÃO INVALIDA.... VOCE DEVE ESCOLHER')
print('\n=========== PAGAMENTO ===========')
print('\n1 - CARTÃO TABAJARA')
print('QUALQUER OUTRA TECLA PARA PAGAMENTO Á VISTA\n')
forma_pgto = input('QUAL FORMA DE PAGAMENTO ? ')
if forma_pgto == '1':
    desconto = valor_compra * 0.05
    preco_final = valor_compra - desconto
    tipo_pgto = 'Cartão Tabajara'
else:
    desconto = 0
    preco_final = valor_compra
    tipo_pgto = 'Pagamento á vista'
print('\n=========== NOTA FISCAL TABAJARA HIPERMERCADO ===========\n')
print('Tipo de Carne:', tipo_carne)
print('Quantidade Comprada:', qtdecarne, 'KG')
print('A Forma de pagamento:', tipo_pgto)   
print("O Valor de desconto foi R$", desconto)
print('O Valor a pagar R$', preco_final)