import pandas as pd
from areas import area
dataFile = pd.read_csv('figuras.csv', sep = '\t')

print("Procesando figuras...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	figura = row['FIGURA']
	m1 = row['MEDIDA1']
	m2 = row['MEDIDA2']
	a = area(figura, m1, m2)
	areas.append(a)
	print(f"Fila {index}: Figura = {row['FIGURA']}, Medida1 = {row['MEDIDA1']}, Medida2 = {row['MEDIDA2']}, Area = {a}")


