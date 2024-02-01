# Obtendo informações de coleções relacionadas: for indice variavel in enumerate(colecao)

alunos = ['Alice','Bob','Carl','Daniele']

notas = [9.5, 8.0, 9.5, 8.0]

for indice, aluno in enumerate(alunos):
    print(f'Nome: {aluno} - Nota: {notas[indice]}')