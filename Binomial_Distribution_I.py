'''
## Tarefa ##

- A proporção de meninos para meninas para bebês nascidos na Rússia é 1.09:1. Se houver criança nascida por nascimento, 
que proporção de famílias russas com exatamente 6 filhos terão pelo menos 3 meninos?
Escreva um programa para calcular a resposta usando os parâmetros acima.

## Formato de entrada ## 

- Uma única linha contendo os seguintes valores: 1.09 1 Se você não deseja ler essas informações de stdin, pode embuti-las em seu programa.

## Formato de Saída ##

- Imprima uma única linha indicando a resposta, arredondada para uma escala de 3 casas decimais (ou seja, formato 12,3).
'''

''' Solução '''

from scipy.special import comb
boysWeight, girlsWeight = map(float, input().split(" "))
prob = boysWeight / (boysWeight + girlsWeight)

def combination(n,k):                        
    return comb(n, k, exact=True)
n=6
result = sum(prob**k * (1-prob)**(n-k) * combination(n, k) for k in range(3, 7))

print(f'{result:.3f}')