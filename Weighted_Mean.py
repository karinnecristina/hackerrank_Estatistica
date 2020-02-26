'''
## Objetivo ## 
No desafio anterior, calculamos uma média. Nesse desafio, praticamos o cálculo de uma média ponderada.

## Tarefa ##
Dada uma matriz X de N números inteiros e uma matriz W representando os respectivos pesos dos X elementos, calcule e imprima a média ponderada dos elementos.

## Formato de entrada ##

A primeira linha contém um número inteiro N, denotando o número de elementos nas matrizes X e W.
A segunda linha contém N números inteiros separados por espaço, descrevendo os respectivos elementos da matriz X.
A terceira linha contém N números inteiros separados por espaço, descrevendo os respectivos elementos da matriz W.

## Formato de Saída ##

Imprima a média ponderada em uma nova linha. Sua resposta deve ser arredondada para uma escala de 1 casa decimal (ou seja, formato 12,3).
'''

''' Solução '''

n_elementos = input()

valores = []
peso = []

valores = input().split(" ")
peso = input().split(" ")

             
valores_int = list(map(int, valores)) 
peso_int = list(map(int, peso)) 

val_pond = []
for i in range(len(valores_int)):
    val_pond.append(valores_int[i] * peso_int[i])
    tot_val_pond = sum(val_pond)
    tot_peso_int = sum(peso_int)
    media_pond = tot_val_pond / tot_peso_int 

print(round(media_pond,1))

