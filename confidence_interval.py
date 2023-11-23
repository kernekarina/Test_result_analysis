import math
from scipy import stats

# Numero de amostras
n = 20

# Grau de liberdade t-student
gl = n - 1

# Nível de confiança
p = 0.90

# Complementar
alpha = 1 - p
#proba = 1 - alpha/2

# Valor tabela student
ts = stats.t.ppf(alpha, gl)
print(f'O valor de t é {ts}')

# Média amostral
x_barra = 0.08682

# desvio amostral
s = 0.001602

# 
tol = ts*s/(math.sqrt(n))
# 
print(f'O intervalo de confiança é {x_barra} +- {tol}')