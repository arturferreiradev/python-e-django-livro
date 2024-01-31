# Suítes de código são o mesmo que os blocos de código em outras linguagens, porém o termo utilizado em Python é diferente

idade = int(input('Qual a sua idade? '))
tem_titulo = input('Possui título de eleitor? [S/N] ')

if(idade >= 16) and (tem_titulo == 'S'):
    print('Vocẽ pode votar.') # Utilizar quatro espaços para identação e não utilizar o tab

if(idade >= 18):
    print('Você é maior de idade')
    print('Você pode comprar bebida alcoólica')

