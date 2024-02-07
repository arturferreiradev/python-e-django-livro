palavra = 'Assessoria de Assuntos Aleatórios'

print('A string original é %s' % palavra)

print('%s tem %d substrings \'ss\'' % (palavra, palavra.count('ss')))

print('%s tem %d substrings \'ss\' ate a posiçao 10' % (palavra, palavra.count('ss', 0, 10)))

print('Usando o método da classe string:')

print('%s tem %d substrings \'ss\'' % (palavra, str.count(palavra,'ss')))

print('%s tem %d substrings \'ss\' ate a posiçao 10' % (palavra,str.count(palavra,'ss', 0, 10)))

