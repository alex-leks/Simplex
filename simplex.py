import math
import numpy as np
from funcoes import *

m = 3 #número de restrições
n = 4 #número de variáveis
c = [] #vetor de custos
b = [] #vetor de recursos
A = [[]] #matriz dos coeficientes das restrições

variaveis_de_folga = True #vê se há necessidade de resolver o simplex com variáveis de folga

if variaveis_de_folga:
    A = resolver_problema_auxiliar()

print("Hello World")