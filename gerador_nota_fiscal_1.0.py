listprovisoria = {}
listaoficial = []
print('-' * 50)
print(' ' * 18, '\033[1;4mCupom fiscal\033[m')
print('-' * 50)
e = 'S'
while e not in 'Nn':
    listprovisoria['produto'] = input('Produto: ')
    listprovisoria['preço'] = float(input('Preço: R$'))
    listprovisoria['codigo'] = input('Código do Produto: ')
    listaoficial.append(listprovisoria.copy())
    listprovisoria.clear()
    e = input('Quer continuar? [S/N]')[0]
print(listaoficial) #Teste
