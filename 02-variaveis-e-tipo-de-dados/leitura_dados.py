# Exemplo de código utilizando input(), para que o usuário interaja com o progama através do teclado, código simples sem verificação se os dados digitados são válidos

print('Cálculo de Volume')
comprimento = float(input('Entre com o comprimento em metros da caixa d\'água: ')) # uso da função float para converter de string para float
largura = float(input('Entre com a largura em metros da caixa d\'água: '))
profundidade = float(input('Entre com a profundidade em metros da caixa d\'água: '))
volume_em_m3 = comprimento * largura * profundidade
volume_em_litros = volume_em_m3 * 1000
print("A caixa d\'água comporta %.2f litros." %volume_em_litros)