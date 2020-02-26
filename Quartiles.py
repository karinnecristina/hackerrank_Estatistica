'''
## Objetivo ##
Neste desafio, praticamos o cálculo de quartis.

 ## Tarefa ##
Dada uma matriz X de N números inteiros, calcule o respectivo primeiro quartil(Q1), segundo quartil(Q2) e terceiro quartil(Q3). É garantido que Q1,Q2 e Q3 são inteiros.

## Formato de entrada ##

A primeira linha contém um número inteiro N, denotando o número de elementos na matriz.
A segunda linha contém N números inteiros separados por espaço, descrevendo os elementos da matriz.

## Formato de Saída ##

Imprima 3 linhas de saída na seguinte ordem:

A primeira linha deve ser o valor de Q1.
A segunda linha deve ser o valor de Q2.
A terceira linha deve ser o valor de Q3.
'''

''' Solução '''

from statistics import median

n_elementos = int(input())
            
elementos = sorted(list(map(int, input().split()))) 

Q1 = int(median(elementos[:n_elementos//2]))
Q2 = median(elementos)
Q3 = int(median(elementos[(n_elementos+1)//2:]))

print(round(Q1))
print(round(Q2))
print(round(Q3))
