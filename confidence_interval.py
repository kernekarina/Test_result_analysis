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
x_barra = 0.08682968421052632

# desvio amostral
s = 0.0016024881000504577

# 
tol = ts*s/(math.sqrt(n))
# 
print(f'O intervalo de confiança é {x_barra} +- {tol}')