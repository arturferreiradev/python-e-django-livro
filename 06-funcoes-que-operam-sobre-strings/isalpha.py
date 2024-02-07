texto = 'TinhaUmaPedraNoMeioDoCaminho'

if texto.isalpha():
    print('O texto %s contém apenas letras' % texto)
else:
    print('O texto %s contém caracteres não alfabéticos' % texto)

texto = 'Tinha 2 pedras no meio do caminho'

if str.isalpha(texto):
    print('O texto %s contém apenas letras' % texto)
else:
    print('O texto %s contém caracteres não alfabéticos' % texto)