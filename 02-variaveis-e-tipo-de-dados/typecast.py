# Typecast : Convertendo tipos de dados

# Função int(),converte em inteiro se possível
a = '1'
x = int(a)

pi = 3.1415926
parte_inteira_de_pi = int(pi)

int(True) # Convertido em 1
int(False) # Convertido em 0

# Função float(), converte em número de ponto flutuante
y = 20
z = float(y) 

# Função complex(), converte em número complexo
w = complex(z) # A parte imaginária será sempre 0

# Função str(), converte em string
codigo = 13
nome_usuario = "Francisco"
hash_usuario = str(codigo) + nome_usuario

# Função set(), converte listas ou tuplas em conjuntos
uma_lista = [1, 2, 3]
uma_tupla =  {'pedra', 'papel', 'tesoura', 'lagarto', 'Spock'}

conjunto_1 = set(uma_lista)
conjunto_2 = set(uma_tupla)

print(conjunto_1)
print(conjunto_2)

letras = set("abacate")
print(letras)

# Função bool(), que converte qualquer valor para True ou False

print(bool([])) # Valores vazios, zeros ou None são convertidas para false, numeros !=0, strings não vazias, coleções não vazias são True
