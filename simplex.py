import math
import numpy as np
from funcoes import *

m = 3 #número de restrições
n = 4 #número de variáveis
c = [] #vetor de custos
b = [] #vetor de recursos
A = [[]] #matriz dos coeficientes das restrições

variaveis_de_folga = True #vê se há necessidade de resolver o simplex com variáveis de folga
ordem_das_variaveis = []
if variaveis_de_folga:
    A = resolver_problema_auxiliar(A)


B = basico(A)
N = nao_basico(A)
c_b = custo_basico(c)
c_nb = custo_nao_basico(c)

BT = transpor(B)
x_b = resolver_sistema(B, b)

#vetor multiplicador simplex
vms = resolver_sistema(BT, c_b)

if custo_relativo():
    break




