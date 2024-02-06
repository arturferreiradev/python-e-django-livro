import random

nomes = ['Alice', 'Bob', 'Carl', 'Daniele', 'Edgard']

for n in range(5):
    random.shuffle(nomes) 
    print(f'Na passagem de número {n + 1} a lista estava assim: {nomes}')

# Obs: no livro mostra a função shuffle conforme o exemplo porém está em desuso na versão 3.9 do Python e foi removida na versão 3.11