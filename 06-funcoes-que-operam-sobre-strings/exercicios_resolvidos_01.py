# Crie um programa que solicita ao usuário que digite o seu login e, em seguida, verifica se esse login está de acordo com as seguintes regras:
# Inicia com uma letra maiúscula.
# Tem, no mínimo, seis caracteres.
# Possui, pelo menos, dois caracteres numéricos.
# Possui, pelo menos, três letras.
# Possui tamanho de até dez caracteres.

login_ok = True

numeros = 0

letras = 0

login = input('Digite o novo login: ')

padrao = login.capitalize()

if login != padrao:
    login_ok = False
    print('O login deve iniciar com uma letra maiúscula.')

if len(login) < 6:
    login_ok = False
    print('O login deve possuir, no mínimo, 6 caracteres.')

for letra in login:
    if letra.isdigit():
        numeros = numeros + 1
        if letra.isalpha():
            letras = letras + 1
    
if letras < 3:
    login_ok = False
    print('O login deve possuir, no mínimo, 3 letras.')

if numeros < 2:
    login_ok = False
    print('O login deve possuir, no mínimo, 2 caracteres numéricos.')

if len(login) > 10:
    login_ok = False
    print('O login deve possuir, no máximo, 10 caracteres.')

if login_ok:
    print(f'O login escolhido, {login}, é valido.')
else:
    print(f'Login invalido!')
            
