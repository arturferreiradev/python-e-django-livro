# A instrução continue serve para ignorar a iteração atual na execução de um loop e voltar para o trecho do código em que sua condição de parada é definida.

while(True):
    letra = input('Digite alguma letra diferente de X (Q para sair) ')
    if(letra == 'X'):
        continue
    elif(letra == 'Q'):
        break
    else:
        print(f'Você digitou letra {letra}')

print('Programa encerrado!')