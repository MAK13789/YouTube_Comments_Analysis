import csv
data_list = []
with open('query_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row[0])
#print (data_list)
#data = [item for sublist in data_list for item in sublist]
#print (data)
print (data_list)