"""
Exercício 2

Um truque bem conhecido para descobrir se um inteiro N é um múltiplo de nove é
computar a soma S dos seus dígitos. Se S é um múltiplo de nove, então N também é.
Este é um teste recursivo e a profundidade da recursão necessária para obter a
resposta para o número N é chamada o grau-9 de N.

Sua tarefa é, dado um inteiro positivo N, determinar se ele é um múltiplo de 
nove e, caso ele seja, qual o seu grau-9.

Exemplos:

Número: 999999999999999999999
Grau-9: 3
Número: 9999999999999999999999999999998
Grau-9: 0
Número: 81:
Grau: 2
Número: 9
Grau: 1

Entrada:
Usando a função 'ler_entrada' você irá ter acesso a uma lista de entradas a serem
testadas, para cada entrada você irá realizar o teste se o número é divisível
por 9 e se for dar como resultado o seu grau-9 se não for deve retornar 0.
A saída será criada usando a função 'salvar_resultado' para cada valor de 
entrada, isto é, o 'salvar_resultado' salva o resultado de apenas 1 número
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
        resultado_str = str(resultado)
        f_saida.write(resultado_str)
        f_saida.write('\n')
