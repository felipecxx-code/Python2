# Exercício 3
""" Escreva um programa que pede para o usuário entrar uma certa quantidade de minutos. O programa deve fazer a conversão dessa quantidade em minutos para o formato hora:minuto. Por exemplo, caso o usuário passe o valor de 80 o programa deve mostrar paro o usuário que isso é equivalente a 1h20m. O seu código deve conter comentários para explicar o que está fazendo nas principais linhas
"""

# Escreva seu código aqui
minutos = int(input('Digite uma quantidade em minutos: '))
horas = minutos // 60 # Valor em horas = Divisão Inteira
horas_minutos = minutos % 60 #Valor em minutos = Restante da divisão

print(f'{minutos} minutos é equivalente a {horas}h{horas_minutos}m')