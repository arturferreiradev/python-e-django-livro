# Quando len() recebe uma string como parâmetro, retorna a quantidade de caracteres dessa string. Mas também pode ser usada para obter a quantidade de itens em uma coleção.
lista = ['A_lista', 'B_lista', 'C_lista']

tupla = ('A_tupla', 'B_tupla', 'C_tupla')

dicionario = {'A_dicionario':'1', 'B_dicionario':'2',
'C_dicionario':'3'}

string = 'Duas uvas'

print('Lista: ', lista, 'tamanho: ', len(lista))

print('Tupla:', tupla, 'tamanho: ', len(tupla))

print('Dicionario:', dicionario, 'tamanho: ', len(dicionario))

print('String:', string, 'tamanho: ', len(string))