import TX_data
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math


#parameters of condition 1
#measured power
power_cond1=[]
for i in range(1,len(TX_data.cond_1)):
    power_cond1.append(float(TX_data.cond_1[i][5]))

media_cond1 = np.mean(power_cond1) 
variancia_cond1 = np.var(power_cond1)
std_dev_cond1 = np.std(power_cond1)

# Numero de amostras
n = len(power_cond1)

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
x_barra = media_cond1

# desvio amostral
s = std_dev_cond1

# 
tol = ts*s/(math.sqrt(n))
# 
print(f'O intervalo de confiança é {x_barra} +- {tol}')

print('Length of the sample with condition 1:',n)
print('Mean (Average) of condition 1:', media_cond1)
print('Variance of condition 1:', variancia_cond1)
print('Standard deviation of condition 1:', std_dev_cond1)


#plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],power_cond1)
#plt.show()