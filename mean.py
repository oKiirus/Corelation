import csv
import pandas as pd
import plotly.express as px
import numpy as np

with open('ice.csv', newline = '') as f:
    file = csv.reader(f)
    data = list(file)
data.pop(0)
df = pd.read_csv('ice.csv')

graph = px.scatter(df, x = 'Coffee', y = 'Sleep')
graph.show()


array = []
sales = []
for i in data:
    array.append(float(i[1]))
    sales.append(float(i[2]))

correlation = np.corrcoef(array, sales)
print(correlation[0, 1])
