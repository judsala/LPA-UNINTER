print('Welcome to my store!')
productPrice = float(input('Entre com o valor do produto: '))
amount = int(input('Entre com a quantidade de produtos: '))
price = productPrice * amount

if(amount < 11):
    fee = 30 
    total = price + fee 
elif(amount >= 11) and (amount < 101):
    fee = 60
    total = price + fee
elif(amount >= 101) and (amount < 1001):
    fee = 120
    total = price + fee
else:
    fee = 240 
    total = price + fee


print('O preço sem frete é: {:.2f}' .format(price))
print('O preço com frete é: {:.2f} (frete de R$ {:.2f})' .format(total, fee))