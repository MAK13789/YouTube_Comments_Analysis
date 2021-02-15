import csv
import random
nounlist = []
with open('nounlist.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        nounlist.append(row[0])
random.shuffle(nounlist)
i = 1
while i <= 7:
    idx = random.randint(0, len(nounlist)-81)
    subset = nounlist[idx:idx+80]
    '''need to delete this subset from nounlist now'''
    k = idx + 80
    while (k >= idx):
        del nounlist[k]
        k -= 1
    filename = 'queries_' + str(i) + '.csv'
    with open(filename, 'w', newline = '') as file:
        writer = csv.writer(file)
        for j in subset:
            writer.writerow([j])
    i += 1