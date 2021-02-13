import csv
import random
data_list = []
with open('nounlist.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row)
data = [item for sublist in data_list for item in sublist]
random.shuffle(data)
#print (data)
#print (len(data))
with open('query_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow([i])