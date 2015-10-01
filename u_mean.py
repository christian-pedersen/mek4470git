
import os
from string import split
import numpy as np
import matplotlib.pyplot as plt



T = 2
dt = 0.005
Nt = T/dt
number_of_calculation_points = 440
folders = np.linspace(0, 2, Nt+1)
umean_x = np.zeros([Nt+1, number_of_calculation_points*10])
umean_y = np.zeros([Nt+1, number_of_calculation_points*10])
kmean = np.zeros([Nt+1, number_of_calculation_points*10])

# collect mean values for all calculation points
for i in folders:
    if i == 0:
        continue
    foldernumber = float(i)
    if i == 1.0:
        foldernumber = 1
    if i == 2.0:
        foldernumber = 2
    folder = str(foldernumber)
    with open( os.path.join(folder,"U")) as filename:
        lines = filename.readlines()[22:4422]
        X, Y = [], []
        for line in lines:
            x, y, z = line[1:-2].split(' ')
            X.append(float(x))
            Y.append(float(y))
    j = int(i/dt)
    umean_x[j] = X
    umean_y[j] = Y
    filename.close()
    with open( os.path.join(folder,"k")) as filename:
        lines = filename.readlines()[22:4422]
        k = []
        for line in lines:
            k.append(float(line))
    kmean[j] = k
    filename.close()


umeanx_per_t = np.zeros(Nt+1)
umeanx_per_t[0] = 10
umeany_per_t = np.zeros(Nt+1)
umeany_per_t[0] = 0
kmean_per_t = np.zeros(Nt+1)
kmean_per_t[0] = 0.375
for i in range(1, int(Nt+1)):
    umeanx_per_t[i] = sum(umean_x[i][:])/float(4400)
    umeany_per_t[i] = sum(umean_y[i][:])/float(4400)
    kmean_per_t[i] = sum(kmean[i][:])/float(4400)

umeanx = sum(umeanx_per_t[:])/len(umeanx_per_t)
umeany = sum(umeany_per_t[:])/len(umeany_per_t)
kmean_ = sum(kmean_per_t[:])/len(kmean_per_t)
print '----------------------------------------'
print 'mean velocity in x-directon: %g' % umeanx
print 'mean velocity in y-directon: %g' % umeany
print 'mean kinetic energy: %g' % kmean_
print '----------------------------------------'


