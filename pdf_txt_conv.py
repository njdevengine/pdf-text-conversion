with open ("kimco.txt", "r") as myfile:
    data=myfile.readlines()
    data = ''.join(data)
print(data)

import pandas as pd
import csv
from scipy.spatial.distance import euclidean, pdist, squareform

with open('kimco.txt', 'r') as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in read:
        print (', '.join(row))
        
df = pd.read_csv('kimco.txt',encoding = "UTF-8", header = None)

squareform(pdist(df, metric='euclidean'))
