# Exercício 4
"""
Analise o seguinte programa abaixo. E faça o que é pedido nos itens:

a) Substitua os comentários em cima de cada linha por uma explicação do que aquela linha faz.
b) Note que a mensagem tem três problemas. O primeiro é que existe um hífen em 'A - Ginasta'. O segundo é que a palavra ginasta aparece com letra maiuscula. E por último, existem dois espaços entre em '... de Andrade  ganhou'. Modifique os valores da variável nome e profissão para corrigir a mensagem.
"""

# A varíavel recebe uma string de nome e profissão
nome_e_profissao = "Rebeca Rodrigues de Andrade - Ginasta"

# Localiza em qual posição no valor da variável nome_e_profissao está o caractere "-".
posicao_hifen = nome_e_profissao.find("-")

# Variável receberá o valor apenas até um caractere antes do hífen de nome_e_profissao
nome = nome_e_profissao[:posicao_hifen]

# Variável receberá o valor depois do hífen de nome_e_profissao 
profissao = nome_e_profissao[posicao_hifen:]

# Adicione código modificar os valores das variáveis nome e profissao de forma a corrigir a mensagem.


# Imprimir variável com a profissão, nome e o feito nas olimpíadas
print(f"A{profissao.replace('-', '') } {nome} ganhou medalha de ouro no solo e prata no individual geral nas olimpíadas de Paris 2024.")