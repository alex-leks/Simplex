import numpy as np

# Funcao que faz a implementacao do metodo do simplex primal
# Funcao que faz a implementacao do metodo do simplex primal
def simplex(m, n, c, A, b):
    # Fase 1: determina uma particao basica factivel: A = [B N]
    B = list(range(n - m, n)) # Faz com que as ultimas m colunas sejam identidade
    N = list(range(0, n - m))

    # Vetor para acompanhar a ordem das variáveis
    v = []
    contador = 1
    for i in range(1, n + 1):
        v.append(i)

    # Matrizes basicas e nao basicas de A
    B_A = A[:, B]
    N_A = A[:, N]
    print("Matriz básica: ")
    print(f"B: {B_A}")
    print("-" * 40)

    print("Matriz não básica: ")
    print(f"N: {N_A}")
    print("-" * 40)

    # Custos de B e N
    print("Custo básico: ")
    c_B = c[B]
    print(c_B)

    print("Custo não básico: ")
    c_N = c[N]
    print(c_N)
    print("-" * 40)

    iteracao = 1
    # Fase 2: inicio da iteracao simplex
    while(True):
        print(f"Iteração {iteracao}")
        iteracao += 1
        # Passo 1: calculo da solucao basica
        x_B = np.linalg.solve(B_A, b)
        print(f"Solução básica: {x_B}")

        # Passo 2: calculo dos custos relativos
        # 2.1: calculo do vetor multiplicador simplex
        lmbd = np.linalg.solve(B_A.T, c_B)
        print(f"Vetor multiplicador simplex: {lmbd}")
        # 2.2: custos relativos
        c_atual = c_N - np.dot(N_A.T, lmbd)
        print(f"Custos relativos: {c_atual}")

        # Passo 3: teste de otimalidade
        if np.all(c_atual >= 0):
            x = np.zeros(n)
            j = 0
            for j, i in enumerate(B):
                x[i] = x_B[j]
            print("Está na solução ótima.")
            return x  # Algoritmo para, se ja estiver no ponto otimo
        
        # 3.1: escolha da variavel para entrar na base
        indice_entr = np.argmin(c_atual)
        print(f"Variável para entrar na base: x{v[indice_entr]}")
        j_A = N_A[:, indice_entr]

        # Passo 4: calculo da direcao simplex
        y = np.linalg.solve(B_A, j_A)
        if np.all(y <= 0):
            print("O problema não tem solução ótima finita")
            exit()
        else:
            print(f"Direção simplex: {y}")

        # Passo 5: determinar tamanho do passo e variavel para sair da base
        indices_positivos = np.arange(m)[y > 0]
        razao = x_B[y > 0] / y[y > 0]
        indice_min = np.argmin(razao)
        indice_sai = indices_positivos[indice_min]
        print(f"Variável para sair da base: x{v[indice_sai + (n-m)]}")

        # Passo 6: nova particao basica
        B[indice_sai], N[indice_entr] = N[indice_entr], B[indice_sai]
        c_B[indice_sai], c_N[indice_entr] = c_N[indice_entr], c_B[indice_sai]
        for i in range(m):
            B_A[i][indice_sai], N_A[i][indice_entr] = N_A[i][indice_entr], B_A[i][indice_sai]
        print("-" * 40)

        # Atualizando o vetor que acompanha a ordem das variáveis 
        indice_v_sai = indice_sai + (n-m)
        v[indice_entr], v[indice_v_sai] = v[indice_v_sai], v[indice_entr]


        # Retorna ao passo 1

# ENTRADA
# Coletando os dados de linha e coluna
print("#" * 40)
print("Solver do método do simplex")
print("#" * 40)
m = int(input("Digite o número de restrições (m): ")) # Numero de linhas
n = int(input("Digite o número de variáveis (n): ")) # Numero de colunas

print("-" * 40)

# Coletando os vetores de custo e recurso
print('Digite os elementos de c:')
c = np.array(list(map(int, input().split())))
assert c.size == n, 'Tamanho incorreto de c'
print("-" * 40)

print('Digite os elementos de b:')
b = np.array(list(map(int, input().split())))
assert b.size == m, 'Tamanho incorreto de b'
print("-" * 40)

# Coletando a matriz dos coeficientes das restricoes
A = np.zeros((m,n))  # Inicializacao de A
print("Digite os elementos da matriz (A):")

for i in range(m):
  le_linha = input().split()
  for j in range(n):
    A[i,j] = le_linha[j]
assert A.shape == (m, n), 'Tamanho incorreto de A'
print("-" * 40)

# CALCULO
x = simplex(m, n, c, A, b)
resposta = np.dot(c, x)

# SAIDA
np.set_printoptions(precision=1, floatmode='fixed')
print("-" * 40)
print(f'O vetor resposta é: {x}')
print(f'O valor da função objetiva é: {resposta}')
