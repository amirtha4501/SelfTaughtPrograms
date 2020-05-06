import csv

movies_list = [
    ["Top Gun", "Risky Business", "Minority Report"], 
    ["Titanic", "The Revenant", "Inception"], 
    ["Training Day", "Man on Fire", "Flight"]
]
with open('movies.csv','w', newline= '') as f:
    write = csv.writer(f, delimiter=',')
    for i in movies_list:
        write.writerow(i)

import csv
data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)