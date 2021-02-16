import time
import csv
from tqdm import tqdm
queries = []
with open('queries_1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        queries.append(row[0])
first = queries[0]
for query in tqdm(queries):
    if query != first:
        print (query)
    time.sleep(0.5)