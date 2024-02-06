# Crie um programa que solicitará ao usuário o resultado do último exercício contábil em uma empresa (ou seja, quanto foi o lucro ou prejuízo). Se o valor for positivo, imprima “houve lucro de R$ <valor fornecido>”, se não, mostre “houve prejuízo de R$ <valor fornecido>”. Lembre-se de que o valor não pode ser negativo (não imprima “o prejuízo foi de R$1.000”, pois isso daria a ideia de que, na verdade, houve lucro nesse valor).

resultado_exercicio = float(input('Entre com o valor do resultado do exercicio contabil anterior: '))

if (resultado_exercicio >= 0):
    print(f'Houve lucro de R$ %.2f' % resultado_exercicio)
else:
    resultado_exercicio = abs(resultado_exercicio)
    print(f'Houve prejuizo de R$ %.2f' % resultado_exercicio)