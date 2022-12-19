import numpy as np
import pandas as pd
import random

x = np.linspace(0,1,71, retstep = True)
y = np.linspace(0,1,71, retstep = True)
z = np.linspace(0,1,71, retstep = True)

x_list = []
y_list = []
z_list = []
for num,i in enumerate(y[0]):
    for j in x[0]:
        if num%2 == 0:
            y_list.append(i + (random.random() *1.0E-3))
            x_list.append(j + (random.random() *1.0E-3))
            z_list.append(j + (random.random() *1.0E-3))
        else:
            y_list.append(i + (random.random() *1.0E-3))
            x_list.append(j + x[1]/2)
            z_list.append(i + (random.random() *1.0E-3))
dataset = pd.DataFrame({'x':x_list,'y':y_list,'z':z_list})
dataset.to_csv("triangle1.txt", sep=" ", index=False)