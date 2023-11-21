import csv
from statistics import median
from statistics import variance
from math import isnan
from itertools import filterfalse
import matplotlib.pyplot as plt
import numpy as np

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


print(len(cond_1))
print(len(cond_2))

#calculo de média
power_cond1=[]
for i in range(1,len(cond_1)):
    power_cond1.append((cond_1[i][6]))
 
print(median(power_cond1))
plt.plot(power_cond1)
plt.bar(power_cond1)
plt.show()


#print(variance(power_cond1))
