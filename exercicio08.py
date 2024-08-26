# Exercício 8
"""
Escreva um programa que inicialize uma variável com o valor 5 para representar o número de milhas. Depois, converta esse valor para quilômetros e depois para metros, usando km = milhas / 0.62137 e metros = 1000 * km. Imprima o resultado na seguinte forma:

milhas
5
km
8.04672
metros
8046.72
"""
milhas = 5

km = milhas / 0.62137

metros = 1000 * km

print(f'milhas \n{milhas}')
print(f'km \n{km:.5f}')
print(f'metros \n{metros:.2f}')

# Usando as fórmulas e método passado, meu valor foi 8.04674 e 8046.74 e não 8.04672 e 8046.72