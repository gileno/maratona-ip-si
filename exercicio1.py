"""
Exercício 1

Todo número inteiro positivo pode ser representado pelo produto de potências 
de números primos (os chamados fatores primos).

Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.

Outros exemplos:
5 = 5 (números primos só tem um fator primo - ele mesmo)
100 = 2 x 2 x 5 x 5
198 = 2 x 3 x 3 x 11
276 = 2 x 2 x 3 x 23

Formato de Entrada/Saída:
Usando a função 'ler_entrada' você receberá uma lista de números a serem testados
e para cada número deverá retornar uma lista com os fatores primos dele, use
a função 'salvar_resultado' para salvar o resultado para cada número
testado, isto é, o 'salvar_resultado' salva o resultado de apenas 1 número
testado.
"""

def ler_entrada():
    entrada = []
    with open('entrada1.txt', 'r') as f_entrada:
        for line in f_entrada:
            entrada.append(int(line))
    return entrada

def salvar_resultado(resultado):
    with open('saida1.txt', 'a') as f_saida:
        resultado_str = ','.join(map(str, resultado))
        f_saida.write(resultado_str)
        f_saida.write('\n')
