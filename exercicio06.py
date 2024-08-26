# Exercício 6

""" Abaixo é apresentada a variável palavra. Com relação ao valor da variável palavra responda:

a) Quantas letras possui essa palavra?

b) Quantas vezes a letra 'o' aparece nessa palavra?

c) Qual a posição da letra v nessa palavra?

d) Escreva essa palavra de trás para frente.

e) Divida essa palavra em duas com a mesma quantidade de caracteres.

Você deve utilizar código python para ajudar a responder essas perguntas.
"""

palavra = "pneumoultramicroscopicossilicovulcanoconiotico"

# Item a
qntd_letras = len(palavra)
print(qntd_letras) # a variável palavra tem 46 letras

# Item b
qntd_letra_o = palavra.count('o')
print(qntd_letra_o) # Total de 9 letras 'o'

# Item c
posicao_letra = palavra.find('v')
print(posicao_letra) # A letra 'v' se encontra na posição 30 da palavra

# Item d
print(palavra[::-1]) #ocitoinoconacluvocilissocipocsorcimartluomuenp

# Item e
print(palavra[:23])   # pneumoultramicroscopico
print(palavra[23:46]) # ssilicovulcanoconiotico

