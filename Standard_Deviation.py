'''
## Objetivo ##
Neste desafio, praticamos o cálculo do desvio padrão.

## Tarefa ##
Dada uma matriz X de N números inteiros, calcule e imprima o desvio padrão. Uma margem de erro de será tolerada para o desvio padrão + OU - 0.1.

## Formato de entrada ##

A primeira linha contém um número inteiro , denotando o número de elementos na matriz.
A segunda linha contém números inteiros separados por espaço, descrevendo os respectivos elementos da matriz.

## Formato da Saída ##

Imprima o desvio padrão em uma nova linha, arredondada para uma escala de 1 casa decimal (ou seja, formato 12,3).
'''

''' Solução '''

from statistics import *

n_elementos = input()
elementos = []

elementos = input().split(" ")
             
elementos_int = list(map(int, elementos)) 

std = pstdev(elementos_int)
print(round(std,1))
