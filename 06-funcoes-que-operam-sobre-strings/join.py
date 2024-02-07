# Esta função recebe como entrada um delimitador e uma coleção de strings e retorna uma string com os itens dessa coleção, concatenados e delimitados pelo caractere fornecido como parâmetro (atenção a este detalhe: se sua coleção contiver algum dado de outro tipo qualquer, ocorrerá um erro).

lista = ['A_lista', 'B_lista', 'C_lista']

tupla = ('A_tupla', 'B_tupla', 'C_tupla')

dicionario = {'A_dicionario':'1', 'B_dicionario':'2',
'C_dicionario':'3'}

separador = '*'

print('Lista:', lista)

print('Tupla:', tupla)

print('Dicionario:', dicionario)

print('Agora, apos o join:')

print('Lista:', separador.join(lista))

print('Tupla:', separador.join(tupla))

print('Dicionario:', separador.join(dicionario))