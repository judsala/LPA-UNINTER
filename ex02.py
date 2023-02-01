print('Welcome to my Ice Cream Shop')
print('-' * 42 + ' Cardápio ' + '-' * 43)
print('| Código | Descrição' + ' ' * 12 + '| Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('-' * 95)

total = 0 

while True: 
    size = input('Entre com o tamanho do pote desejado (P/M/G): ') 
    size = size.upper() 

    code = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ') 
    code = code.upper() 

    if (size != 'P' and size != 'M' and size != 'G'): 
        print('!' * 7 + 'TAMANHO ou CÓDIGO INVÁLIDO(S)' + '!' * 7) 
        continue 
    if (code != 'TR' and code != 'ES' and code != 'PR'):
        print('!' * 7 + 'TAMANHO ou CÓDIGO INVÁLIDO(S)' + '!' * 7)
        continue

    if (size == 'P' and code == 'TR'): 
        print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00 reais') 
        total += 6 
    elif (size == 'P' and code == 'ES'):
        print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00 reais')
        total += 7
    elif (size == 'P' and code == 'PR'):
        print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00 reais')
        total += 8
    elif (size == 'M' and code == 'TR'):
        print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00 reais')
        total += 10
    elif (size == 'M' and code == 'ES'):
        print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00 reais')
        total += 12
    elif (size == 'M' and code == 'PR'):
        print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00 reais')
        total += 14
    elif (size == 'G' and code == 'TR'):
        print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00 reais')
        total += 18
    elif (size == 'G' and code == 'ES'):
        print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00 reais')
        total += 21
    elif (size == 'G' and code == 'PR'):
        print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00 reais')
        total += 24

    cont = input('Deseja pedir mais alguma coisa? (S/N) ') 
    cont = cont.upper() 
    if (cont == 'S'):
        continue 
    else:
        print('O total a ser pago é: R${:.2f}' .format(total)) 
        break 
