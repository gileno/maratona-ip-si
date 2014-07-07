"""
Exercício 3
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre 
três possíveis itens: Pedra, Papel ou Tesoura.
O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores 
informa o resultado da partida.

As regras são as seguintes:
Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra

Entrada:
Você deverá usar a função 'ler_entrada' que irá retornar uma lista de jogadas de
Jokenpo, cada jogada é composta por 2 valores, o valor do jogador 1 e o valor do
jogador 2. Para cada jogada você deverá usar a função 'salvar_resultado'
informando 0 para empate, 1 para o caso do jogador 1 ter ganho ou 2 para o caso
do jogador 2 ter ganho.
"""

def ler_entrada():
    entrada = []
    with open('entrada3.txt', 'r') as f_entrada:
        for line in f_entrada:
            entrada.append(line.split(','))
    return entrada

def salvar_resultado(resultado):
    with open('saida3.txt', 'a') as f_saida:
        resultado_str = str(resultado)
        f_saida.write(resultado_str)
        f_saida.write('\n')
