frase = 'Ser ou não ser, eis a questão'

print('Usando o método da classe:')

print('Procurando pela substring \'algo\' dentro da frase %s...' % frase)

substring = 'algo'

posicao = str.find(frase, substring)

if (posicao != -1):
    print(f'Encontrada na posição {posicao}!')
else:
    print('Substring não encontrada!')

print('Procurando pela substring \'ser\' dentro da frase %s...' % frase)

substring = 'ser'

posicao = str.find(frase, substring)

if (posicao != -1):
    print(f'Encontrada na posiçao {posicao}!')
else:
    print('Substring nao encontrada!')

print('Usando um objeto:')

print('Procurando pela substring \'algo\' dentro da frase %s...' % frase)

substring = 'algo'

posicao = frase.find(substring)

if (posicao != -1):
    print(f'Encontrada na posiçao {posicao}!')
else:
    print('Substring nao encontrada!')

print('Procurando pela substring \'ser\' dentro da frase %s...' % frase)

substring = 'ser'

posicao = frase.find(substring)

if (posicao != -1):
    print(f'Encontrada na posição {posicao}!')
else:
    print('Substring não encontrada!')