# Crie um programa que solicita ao usuário cinco nomes de alunos e suas respectivas notas e imprime a média do grupo, usando uma lista para armazenar os nomes e outra para guardar as notas dos estudantes.

nomes = ['', '', '', '', '']
notas = [0.0, 0.0, 0.0, 0.0, 0.0]

for contador in range(5):
    print(f'Entre com o nome do aluno {contador + 1}: ')
    nomes[contador] = input()
    print(f'Entre com a nota do aluno {nomes[contador]}: ')
    notas[contador] = float(input())

media = (notas[0] + notas[1] + notas [2] + notas[3] + notas[4]) / 5

print(f'A média da turma é {media}')