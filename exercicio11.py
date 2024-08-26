# Exercício 11
"""
Dado o texto na variável mensagem, faça um programa que conta a porcentagem de vogais em relação a todos os caracteres da string (espaços e pontuações devem ser contabilizado na porcentagem). Seu programa deve ter comentários. (Cuidado com as vogais maiúsculas)"""

mensagem = "A importancia da persistencia no aprendizado de programacao nao pode ser subestimada. Assim como em qualquer outra habilidade, a pratica constante e a dedicacao sao fundamentais para alcançar a proficiencia. Inicialmente, a complexidade de certas linguagens e conceitos pode parecer desafiadora, mas com o tempo e a experiencia, o aprendizado se torna mais intuitivo e gratificante."

texto_min = mensagem.lower() # Texto foi transformado em minúsculo para facilitar a contagem.
vogais_a = texto_min.count('a') # Contagem da vogal a
vogais_e = texto_min.count('e') # Contagem da vogal e
vogais_i = texto_min.count('i') # Contagem da vogal i
vogais_o = texto_min.count('o') # Contagem da vogal o
vogais_u = texto_min.count('u') # contagem da vogal u

soma = vogais_a + vogais_e + vogais_i + vogais_o + vogais_u # Soma apartir da contagem das vogais a,e,i,o,u
total_texto = len(mensagem) # Total dos caracteres presente no texto
porcentagem_vogais = (soma / total_texto) * 100 # Fórmula para porcentagem
print(f'{porcentagem_vogais:.2f}% são vogais em relação a todos os caracteres') # Resultado em porcentagem das vogais presentes no texto