import random

string = 'abacate laranja tomate'

print(random.choice(string))

lista = ['abacate','laranja','tomate']

print(random.choice(lista))

tupla = ('abacate','laranja','tomate')

print(random.choice(tupla))

print(random.randrange(1, 50, 3)) # randrage parametros: inicio, fim e salto, aceita apenas números inteiros
