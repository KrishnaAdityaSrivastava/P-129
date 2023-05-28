import pandas as pd
import csv

dataset1 = []
dataset2 = []

with open("converted_data.csv" , "r") as f:
    for r in csv.reader(f):
        dataset1.append(r)
        

with open("star1_bright.csv" , "r") as f:
    for r in csv.reader(f):
        dataset2.append(r)


header1 = dataset1[0]
header2 = dataset2[0]

headers = header1 + header2

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

planet_data = []

for i in planet_data1:
    planet_data.append(i)

for j in planet_data2:
    planet_data.append(j)

with open("Final_Final.csv", "a+") as f:
    data = csv.writer(f)
    data.writerow(headers)
    data.writerows(planet_data)



