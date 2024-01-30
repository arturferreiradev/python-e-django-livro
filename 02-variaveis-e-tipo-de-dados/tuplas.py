# Tuplas são estruturas de dados invariáveis

tupla_frutas = ('laranja', 'mamão', 'abacaxi', 'melão') # após criado uma tupla seus dados não podem ser alterados ou removidos, porém é possível trocar uma tupla inteira por outra, direcionando a tupla para um novo endereço de memória que descartará o antigo

print(tupla_frutas)

print(tupla_frutas[1])

del tupla_frutas # deletar a tupla