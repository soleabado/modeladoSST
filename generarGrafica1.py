import pandas as pd
import matplotlib.pyplot as plt
import os

# ****************** CASO 1: 100 nodos HALO3D  Lineal ****************** (done)
'''
file1 = 'emberhalo3d_100nodos_dragon_linear'
file2 = 'emberhalo3d_100nodos_fattree_linear'
file3 = 'emberhalo3d_100nodos_hyperX_linear'
'''

# ****************** CASO 2: 100 nodos HALO 3D Random ****************** (done)

'''
file1 = "emberhalo3d_100nodos_dragon_random"
file2 = "emberhalo3d_100nodos_fattree_random"
file3 = "emberhalo3d_100nodos_hyperX_random"
'''

# ****************** CASO 3: 100 nodos SWEEP 3D Lineal ******************
file1 = 'embersweep3d_100nodos_dragon_linear'
file2 = 'embersweep3d_100nodos_fattree_linear'
file3 = 'embersweep3d_100nodos_hyperX_linear'


# ****************** CASO 4: 100 nodos SWEEP 3D Random ****************** (done)

'''
file1 = 'embersweep3d_100nodos_dragon_random'
file2 = 'embersweep3d_100nodos_fattree_random'
file3 = 'embersweep3d_100nodos_hyperX_random'
'''

# ****************** CASO 5: 576 nodos HALO3D Lineal ****************** (done)
'''
file1 = "emberhalo3d_576nodos_dragon_linear"
file2 = "emberhalo3d_576nodos_fattree_linear"
file3 = "emberhalo3d_576nodos_hyperX_linear"
'''

# ****************** CASO 6: 576 nodos HALO3D Random ****************** (done)

'''
file1 = "emberhalo3d_576nodos_dragon_random"
file2 = "emberhalo3d_576nodos_fattree_random"
file3 = "emberhalo3d_576nodos_hyperX_random"
'''


# ****************** CASO 7: 576 nodos SWEEP 3D Lineal ****************** (done)
'''
file1 = "embersweep3d_576nodos_dragon_linear"
file2 = "embersweep3d_576nodos_fattree_linear"
file3 = "embersweep3d_576nodos_hyperX_linear"
'''

# ****************** CASO 8: 576 nodos SWEEP 3D Random****************** (done)
'''
file1 = "embersweep3d_576nodos_dragon_random"
file2 = "embersweep3d_576nodos_fattree_random"
file3 = "embersweep3d_576nodos_hyperX_random"
'''

# ****************** CASO 9: 1024 nodos HALO3D  Lineal ****************** (done)

'''
file1 = 'emberhalo3d_1024nodos_dragon_linear'
file2 = 'emberhalo3d_1024nodos_fattree_linear'
file3 = 'emberhalo3d_1024nodos_hyperX_linear'
'''

# ****************** CASO 10: 1024 nodos HALO 3D Random ****************** (done)

'''
file1 = "emberhalo3d_1024nodos_dragon_random"
file2 = "emberhalo3d_1024nodos_fattree_random"
file3 = "emberhalo3d_1024nodos_hyperX_random"
'''

# ****************** CASO 11: 1024 nodos SWEEP 3D Lineal ****************** (done)
'''
file1 = 'embersweep3d_1024nodos_dragon_linear'
file2 = 'embersweep3d_1024nodos_fattree_linear'
file3 = 'embersweep3d_1024nodos_hyperX_linear'
'''

# ****************** CASO 12: 1024 nodos SWEEP 3D Random ****************** (done)

'''
file1 = 'embersweep3d_1024nodos_dragon_random'
file2 = 'embersweep3d_1024nodos_fattree_random'
file3 = 'embersweep3d_1024nodos_hyperX_random'
'''
color_texto = "\033[92m"
color_usuario = "\033[0m"

data1 = pd.read_csv(f'{file1}.csv', delimiter=",")
#data1.to_excel(f'./estadisticas/{file1}.xlsx', header=None)
data2 = pd.read_csv(f'{file2}.csv', delimiter=",")
#data2.to_excel(f'./estadisticas/{file2}.xlsx', sheet_name='pag', engine='openpyxl')
data3 = pd.read_csv(f'{file3}.csv', delimiter=",")
#data3.to_excel(f'./estadisticas/{file3}.xlsx', header=None)

filtered_data1 = data1[data1['ComponentName'].str.startswith('rtr')]
filtered_data2 = data2[data2['ComponentName'].str.startswith('rtr')]
filtered_data3 = data3[data3['ComponentName'].str.startswith('rtr')]

color1 = 'lightblue'
color2 = 'pink'
color3 = 'lavender'

fig, ax = plt.subplots()

ax.barh(filtered_data1[' StatisticName'], filtered_data1[' Count.u64'], color=color1, label='dragon')
ax.barh(filtered_data2[' StatisticName'], filtered_data2[' Count.u64'], color=color2, label='fattree')
ax.barh(filtered_data3[' StatisticName'], filtered_data3[' Count.u64'], color=color3, label='hyperX')

# Configura el eje y las etiquetas
plt.subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.1)
ax.set_ylabel('Estadística')
ax.set_xlabel('Valores')

print(color_texto + "Introduce el título para tu gráfica" + color_usuario)
title = input()
ax.set_title(title)


ax.set_title(title)
ax.invert_yaxis()
ax.legend()

plt.savefig(f'{title}.png')

plt.show()

