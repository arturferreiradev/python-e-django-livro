# Agora, escreva um trecho de código que pergunta ao usuário se deseja sair do sistema, com opções “S” e “N”. Caso ele responda “S”, imprima “Você saiu do sistema”; se responder “N”, imprima “Você continua no sistema” e, em qualquer outro valor, “Opção inválida”.

opcao = input('Deseja realmente sair do sistema [S/N]? ')

if(opcao=='S'):
    print('Você saiu do sistema.')
elif(opcao=='N'):
    print('Você continua no sistema.')
else:
    print('Opção inválida!')