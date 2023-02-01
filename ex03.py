print('\n' + 'x' * 68)
print('Welcome to my Cleaning Service Company')
print('x' * 68 + '\n')

def house_size(): #função para receber e validar a metragem do imóvel
    while True: 
        try: 
            x = int(input('Entre com a metragem da casa: ')) 
            if ((x >= 30) and (x < 300)): 
                print('Será necessário(a) 1 funcionário(a) para a limpeza\n') 
                return (x * 0.3) + 60 
            elif ((x >= 300) and (x < 700)):
                print('Serão necessários(as) 2 funcionários(as) para a limpeza\n')
                return (x * 0.5) + 120 
            else:
                print('!! Não aceitamos casas com metragem menor que 30m2 ou maior que 700m2') 
                continue 
        except ValueError: 
            print('Entrada inválida! Digite um valor válido entre 30 e 700m2.\n') 

def cleaning_type(): #função para receber e validar o tipo de limpeza
    while True: 
        x = input('Entre com o tipo de limpeza:\n' + 
                'B - Básica - Indicada para sujeiras semanais ou quinzenais\n' +
                'C - Completa - Indicada para sujeiras antigas e/ou não rotineiras\n' +
                '>> ')
        if ((x == 'B') or (x == 'b')): 
            print('Você selecionou a limpeza BÁSICA\n') 
            return 1 
        elif ((x == 'C') or (x == 'c')):
            print('Você selecionou a limpeza COMPLETA\n')
            return 1.3
        else:
            print('!!! Opção inválida !!!') 
            continue 

def extra_cleaning(): #função para o usuário incluir serviços adicionais
    sum = 0 
    while True: 
        x = input('Deseja mais algum adicional?\n' + 
                '0 - Não desejo mais nada (encerrar)\n' +
                '1 - Passar 10 peças de roupas - R$10,00\n' +
                '2 - Limpar 1 forno/microondas - R$12,00\n' +
                '3 - Limpar 1 geladeira/freezer - R$20,00\n' +
                '>> ')

        if x == '1':
            sum += 10 
            continue 
        elif x == '2':
            sum += 12
            continue
        elif x == '3':
            sum += 20
            continue
        elif x == '0': 
            print('Encerrando programa... Obrigada pela preferência!\n') 
            return sum 
        else:
            print('!!! Digite uma opção válida !!!\n') 
            continue 

print('_' * 18 + ' Menu 1 de 3 - Metragem Limpeza ' + '_' * 18)
size = house_size() 
print('x' * 68)
print('_' * 18 + ' Menu 2 de 3 - Tipo de Limpeza ' + '_' * 18)
option = cleaning_type() 
print('x' * 68)
print('_' * 18 + ' Menu 3 de 3 - Adicional de Limpeza ' + '_' * 18)
additional = extra_cleaning() 
print('x' * 68)
total = (size * option) + additional 
print('TOTAL: R${:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f})' .format(total, size, option, additional))
print('x' * 68) 