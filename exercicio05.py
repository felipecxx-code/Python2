# Exercício 5
"""
Escreva um programa que peça para o usuário dois números a e b. Depois disso o programa deve imprimir as seguintes linhas:

a = 
b =
a + b = 
a**b = 
a - b = 


Do lado direito do sinal de igual deve aparecer o valor referente a conta do que aparece do lado esquerdo. O exemplo do primeiro print já está feito.
"""

# Troque os valores None para receber dados de entrada do usuário.
a = int(input('Digite um número:'))
b = int(input('Digite outro número: '))

# Exemplo da primeira saída que deve ser impressa
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b)
print("a**b = ", a**b)
print("a - b = ", a - b)