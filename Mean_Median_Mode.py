'''
## Objetivo ##
Neste desafio, praticamos o cálculo da média , mediana e da moda.

## Tarefa ##
Dada uma matriz X de N números inteiros, calcule e imprima a respectiva média , mediana e moda em linhas separadas.

## Formato de entrada ##

A primeira linha contém um número inteiro N, denotando o número de elementos na matriz.
A segunda linha contém N números inteiros separados por espaço, descrevendo os elementos da matriz.

## Formato de saída ##

Imprima 3 linhas de saída na seguinte ordem:

Imprimir a média em uma nova linha, a uma escala de 1 casa decimal (ou seja, 12,7).
Imprimir a mediana em uma nova linha, a uma escala de 1 casa decimal (ou seja, 12,7).
Imprima a moda em uma nova linha; se mais de um valor existir, imprima o menor numericamente.
'''

''' Solução '''

from collections import Counter
from statistics import *
from scipy import stats as s
n_elementos = input()

lista = []

lista = input().split(" ")
y = list(map(int, lista))

mode = Counter(sorted(y)).most_common(1)[0][0]

print(mean(y))
print(median(y))
print(mode)