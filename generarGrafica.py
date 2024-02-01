import pandas as pd
import matplotlib.pyplot as plt
import os

'''
cd 'Desktop\TFG\03-10-2023(Evaluating Trade-offs)'
'''

color_texto = "\033[92m"
color_usuario = "\033[0m"
print(color_texto  + "Introduce el directorio en el que se encuentran los .csv: " + "\033[0m")
directorio = input()
files = [0,0,0]
data = [0,0,0]
sim_times = [0,0,0]
categories = [0,0,0]
labels = [0,0,0]

colores = ['lightblue', 'pink', 'mediumpurple']
i = 0

for archivo in os.listdir(directorio):
    path = os.path.join(directorio, archivo)
    if os.path.isfile(path) and path.__contains__('.csv'):
        files[i] = archivo
        print(f'file: {files[i]}')
        i+=1

print(color_texto + "Leyendo..." + color_usuario)
data[0] = pd.read_csv(f'{directorio}\{files[0]}', delimiter=",")
#data1.to_excel(f'./estadisticas/{files[0]}.xlsx', header=None)
data[1] = pd.read_csv(f'{directorio}\{files[1]}', delimiter=",")
#data2.to_excel(f'./estadisticas/{files[1]}.xlsx', sheet_name='pag', engine='openpyxl')
data[2] = pd.read_csv(f'{directorio}\{files[2]}', delimiter=",")
#data3.to_excel(f'./estadisticas/{files[2]}.xlsx', header=None)

print(color_texto + "Filtrando..." + color_usuario)
i = 0
for d in data:
    sim_times[i] = d[' SimTime'][0]
    i += 1

#Sacando nombres
i = 0
for f in files:
    if f.__contains__('dragon'):
        labels[i] = "Dragonfly: \n" + str(sim_times[i])
    elif f.__contains__('fat'):
        labels[i] = "Fattree: \n" + str(sim_times[i])
    else:
        labels[i] = "HyperX: \n" + str(sim_times[i])
    i += 1
print(sim_times)
fig, ax = plt.subplots()
plt.subplots_adjust(right=0.933, left=0.198)
ax.bar(labels, sim_times, color = colores)

plt.yscale('log')


print(color_texto + "Introduce el título para tu gráfica en " + directorio + color_usuario)
title = input()
ax.set_title(title)


plt.savefig(f'{title}.png')
plt.show()

