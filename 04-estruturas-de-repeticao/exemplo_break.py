# As instruções break e continue são usadas para alterar o comportamento de um loop durante sua execução. Quando o interpretador Python estiver executando um loop e chegar a uma instrução break, o loop será encerrado imediatamente e o programa continuará na primeira instrução após o suíte do loop em execução (se não houver mais nenhuma instrução, o programa será encerrado).

x = 0
while(x < 10):
    x = x +1
    if(x == 5):
        break
    print(f'x = {x}')

print('O programa terminou')