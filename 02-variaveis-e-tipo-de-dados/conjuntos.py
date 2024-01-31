# Tipo de dados Set é uma coleção de dados sem relação de ordem entre seus elementos, não permite elementos duplicados pode ser declarado através da função set(), ou declarando os elementos entre chaves

A = {1, 2, 3}
B = {3, 2, 1, 3}

print(A == B) # resultado será True pois a ordem não importa, e a duplicidade não existe

# Testando relações de pertinência
x = 1
print(x in A) # verifica se o x pertence ao conjunto A
print(x not in A) # verifica se o x nao pertence ao conjunto A

print (A|B) # A.union(B) Retorna o conjunto da união de A com B
A|=B # A.update(B) Realiza a uniao de A com B, atribuindo esse valor a A
A&B # A.intersection(B) Retorna a intercesão de A com B
A&=B # A.intersetion_update(B) Intercesão de A com B, atribuindo esse valor a A
A-B # A.difference(B) Retorna a diferença entre A e B
A-=B # A.difference_update(B) Diferença entre A e B, atribuindo esse valor a A
A^B # A.symmetric_difference(B) Diferença simétirica entre A e B
A^=B # A.symmetric_difference_update(B), Diferença simétirica entre A e B, atribuindo esse valor a A
A<=B # A.issubset(B), Retorna True se A for subconjunto de B e False se A está contido em B
A>=B # A.issupperset(B), Retorna True se A for superconjunto de B, e False se A contém B
A<B  # A está contido propriamente em B
A>B # A contém propriamente B

conjunto_vazio = set() # Criando um conjunto vazio
