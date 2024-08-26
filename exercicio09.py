# Exercício 9

"""
Abaixo são apresentadas algumas frases da forma
  Se [sentenca0] então [sentenca1] 

Para cada uma dessas frases transforme elas em variáveis booleanas no python e mostra um exemplo em que a [sentenca1] é verdadeira e outra que ela é falsa. A primeira frase está resolvida como exemplo.

"""

# Exemplo
print("Se é fim de semana e meus amigos estão disponíveis então eu vou a praia")

# Verdadeira
e_fim_de_semana = True
amigos_disponiveis = True
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Falsa
e_fim_de_semana = True
amigos_disponiveis = False
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Item a
print("\nSe eu estudar e fazer os exercícios então eu passo na prova")

# Verdadeira
se_eu_estudar = True
fazer_exercicios = True
passo_na_prova = se_eu_estudar and fazer_exercicios
print("passo_na_prova = ", passo_na_prova)

# Falsa
se_eu_estudar = False
fazer_exercicios = True
passo_na_prova = se_eu_estudar and fazer_exercicios
print("passo_na_prova = ", passo_na_prova)

# Item b
print("\nSe eu tenho um carro ou tenho uma bicicleta então eu posso viajar")

# Verdadeira
tenho_carro = True
tenho_bicicleta = True
posso_viajar = tenho_carro or tenho_bicicleta
print("posso_viajar = ", posso_viajar)

# Falsa
tenho_carro = False
tenho_bicicleta = False
posso_viajar = tenho_carro or tenho_bicicleta
print("posso_viajar = ", posso_viajar)

# Item c
print("\nSe estou cansado ou é tarde então eu vou dormir")

# Verdadeira
estou_cansado = True
esta_tarde = False
eu_vou_dormir = estou_cansado or esta_tarde
print("Eu_vou_dormir: ", eu_vou_dormir)

# Falso
estou_cansado = False
esta_tarde = False
eu_vou_dormir = estou_cansado or esta_tarde
print("Eu_vou_dormir: ", eu_vou_dormir)

# Item d
print("\nSe eu tenho dinheiro e tempo então eu vou viajar")

# Verdadeiro
eu_tenho_dinheiro = True
tenho_tempo = True
eu_vou_viajar = eu_tenho_dinheiro and tenho_tempo
print("Eu_vou_viajar: ", eu_vou_viajar)

# Falso
eu_tenho_dinheiro = True
tenho_tempo = False
eu_vou_viajar = eu_tenho_dinheiro and tenho_tempo
print("Eu_vou_viajar: ", eu_vou_viajar)

