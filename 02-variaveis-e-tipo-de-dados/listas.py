# O Python possui quatro tipos de dados para lidar com coleções
# Listas: Seus itens tem uma ordem entre si, pode armazenar diferentes tipos de dados

lista_frutas = ['laranja', 'mamão', 'abacaxi', 'melão']

print(lista_frutas)

print(lista_frutas[0]) # retorna o indice definido entre [] na lista

print(lista_frutas[3]) # obs: a posicao selecionada pelo indice deve existir previamente na lista

lista_verduras = ['alface', 'tomate', 'cebola']

# Uma lista pode armazenar outras
lista_compras = [lista_frutas, lista_verduras] # Teoria dos conjuntos

print(lista_compras)

# criamos uma estrutura de dados bidimensional, para puxar seus dados devemos incluir dois indices para pegar os dados da lista 1 ou 2
print(lista_compras[0][1])

# Se solicitar com apenas um indice imprimirá apenas uma das listas
print(lista_compras[1])




