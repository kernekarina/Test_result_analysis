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

    #433MHz
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
    #470
    cond_9=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_9.append(data[i])
    cond_10=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_10.append(data[i])
    cond_11=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_11.append(data[i])
    cond_12=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_12.append(data[i])
    cond_13=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_13.append(data[i])
    cond_14=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_14.append(data[i])
    cond_15=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_15.append(data[i])
    cond_16=[]
    for i in range(1, len(data)):
            if int(data[i][1])==470 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_16.append(data[i])
    #868
    cond_17=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_17.append(data[i])
    cond_18=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_18.append(data[i])
    cond_19=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_19.append(data[i])
    cond_20=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_20.append(data[i])
    cond_21=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_21.append(data[i])
    cond_22=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_22.append(data[i])
    cond_23=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_23.append(data[i])
    cond_24=[]
    for i in range(1, len(data)):
            if int(data[i][1])==868 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_24.append(data[i])
    #915
    cond_25=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_25.append(data[i])
    cond_26=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_26.append(data[i])
    cond_27=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_27.append(data[i])
    cond_28=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_28.append(data[i])
    cond_29=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_29.append(data[i])
    cond_30=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_30.append(data[i])
    cond_31=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_31.append(data[i])
    cond_32=[]
    for i in range(1, len(data)):
            if int(data[i][1])==915 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_32.append(data[i])
    
    #923
    cond_33=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_33.append(data[i])
    cond_34=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_34.append(data[i])
    cond_35=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_35.append(data[i])
    cond_36=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_36.append(data[i])
    cond_37=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_37.append(data[i])
    cond_38=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_38.append(data[i])
    cond_39=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==0:
                cond_39.append(data[i])
    cond_40=[]
    for i in range(1, len(data)):
            if int(data[i][1])==433 and int(data[i][2])==22 and int(data[i][3])==12 and int(data[i][4])==2:
                cond_40.append(data[i])


