# Implementando do...while com o loop while, devido a simplicidade do Python não é necessário um do while quando se pode fazer isso usando o while e uma variável de controle

continua = 'S'
somatorio = 0.0
quantidade = 0

while(continua == 'S'):
    preco = (float(input('Entre com o preço do próximo produto: ')))
    somatorio = somatorio + preco
    continua = input('Acrescentar produtos?(S/N) ')

print('O valor dos produtos é R$ %.2f' % somatorio)