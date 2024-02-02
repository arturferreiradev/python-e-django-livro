# Loops aninhados, você pode aninhar loops do mesmo tipo ou de tipos diferentes.

camisetas = ['azul', 'vermelha', 'amarela']
shorts = ['branco', 'preto']
x = 0
y = 0

for x in range(3):
    for y in range(2):
        print(f'Voce pode combinar uma camiseta {camisetas[x]} com um {shorts[y]}')