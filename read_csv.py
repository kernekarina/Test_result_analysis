import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
import math
#from scipy import stats

with open("TX.csv","r") as csv_file:
    file=csv.reader(csv_file,delimiter=";")

    data=[]
    for row in file:
        data.append(row)

    #creating the separated data for each condition

    cond_1=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_1.append(data[i])

    cond_2=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_2.append(data[i])


print('numero de amostras com condição 1:',len(cond_1))
print('numero de amostras com condição 2:',len(cond_2))

#calculo de média
power_cond1=[]
for i in range(1,len(cond_1)):
    power_cond1.append(float(cond_1[i][6]))


media_cond1 = np.mean(power_cond1)
variancia_cond1 = np.var(power_cond1)
std_dev_cond1 = np.std(power_cond1)

print('Média condição 1:',media_cond1)
print('Variância condição 1:', variancia_cond1)
print('Desvio padrão condição 1:',std_dev_cond1)


plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],power_cond1)
plt.show()


#print(variance(power_cond1))
