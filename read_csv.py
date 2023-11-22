import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
import math


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
    cond_3=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_3.append(data[i])
    cond_4=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_4.append(data[i])
    cond_5=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_5.append(data[i])
    cond_6=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_6.append(data[i])
    cond_7=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_7.append(data[i])
    cond_8=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_8.append(data[i])



#parameters of condition 1
power_cond1=[]
for i in range(1,len(cond_1)):
    power_cond1.append(float(cond_1[i][5]))

media_cond1 = np.mean(power_cond1)
variancia_cond1 = np.var(power_cond1)
std_dev_cond1 = np.std(power_cond1)

print('Length of the sample with condition 1:',len(cond_1))
print('Mean (Average) of condition 1:', media_cond1)
print('Variance of condition 1:', variancia_cond1)
print('Standard deviation of condition 1:', std_dev_cond1)


plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],power_cond1)
plt.show()


#print(variance(power_cond1))
