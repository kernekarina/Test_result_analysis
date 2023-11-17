import csv

with open("TX_LoRa.csv","r") as csv_file:
    file=csv.reader(csv_file,delimiter=";")

    data=[]
    for row in file:
        data.append(row)

    cond_1=[]
    for i in range(1, len(data)):
        #for j in range(len(data[1])):
            if int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_1.append(data[i])

print(len(cond_1))