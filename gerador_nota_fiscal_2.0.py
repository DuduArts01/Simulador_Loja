print('-' * 50)
print(' ' * 18, '\033[1;4mCupom fiscal\033[m')
print('-' * 50)

def gerar():
    nota = {}
    nota['produto'] = input('Produto: ')
    nota['preço'] = float(input('Preço: R$'))
    nota['codigo'] = input('Código do Produto: ')
    return nota

nota = gerar()
for i in nota.items():
    print(i)
