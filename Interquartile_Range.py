'''
## Objetivo ##
Neste desafio, praticamos o cálculo do intervalo interquartil. Recomendamos que você complete o desafio Quartis antes de tentar esse problema.

## Tarefa ##
O intervalo interquartil de uma matriz é a diferença entre seus primeiro(Q1) e terceiro(Q3) quartis (ou seja, Q3 - Q1).

Dado um array de X inteiros e um array F representando as respectivas frequências dos X elementos de s, construa um conjunto de dados S, onde cada um ocorre na frequência.

Dica: Cuidado para não usar a divisão inteira ao calcular a média dos dois elementos do meio para um conjunto de dados com um número par de elementos e certifique-se de não incluir a mediana nos conjuntos de dados superior e inferior.

## Formato de entrada ## 

A primeira linha contém um número inteiro N, denotando o número de elementos nas matrizes X e F.
A segunda linha contém N números inteiros separados por espaço, descrevendo os respectivos elementos da matriz X.
A terceira linha contém N números inteiros separados por espaço, descrevendo os respectivos elementos da matriz F.

## Formato de Saída ##

Imprima o intervalo interquartil para o conjunto de dados expandido em uma nova linha. Arredonde sua resposta para uma escala de 1 casa decimal (ou seja, formato 12,3).
'''

''' Solução '''

from statistics import median

n_elements = int(input())
 
elements = list(map(int, input().split()))
freq = list(map(int, input().split()))

new_elements = []
for i in range(n_elements):
    new_elements += [elements[i]] * freq[i]
    new_elements.sort()
tot_freq = sum(freq)

if n_elements%2 != 0:
    Q1 = median(new_elements[:tot_freq//2])
    Q3 = median(new_elements[(tot_freq+1)//2:])
else:
    Q1 = int(median(new_elements[:tot_freq//2]))
    Q3 = int(median(new_elements[tot_freq//2:]))

IQR = round(float(Q3-Q1), 1)
print(IQR)

