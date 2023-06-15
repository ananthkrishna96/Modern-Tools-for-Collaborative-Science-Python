#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Anantha Krishnan O M
"""

# Compute the distance matrix and compute the efficiency associated to the distance matrix for MNIST data

import numpy as np
import matplotlib.pyplot as plt


arc = np.load('mnist.npz')

x_train = arc['arr_0']
y_train = arc['arr_1']
x_test  = arc['arr_2']
y_test  = arc['arr_3']

def d_infty(a, b):
    return np.max(np.abs(b - a))

def d_one(a, b):
    return np.sum(np.abs(b - a))

def d_two(a, b):
    return np.sqrt(np.sum(np.square(b - a)))

def dist_mat(N, dist, x_train):
    Dis = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            d = dist(x_train[i], x_train[j])
            Dis[i, j] = d
            Dis[j, i] = d
    return Dis

def alg_efficiency(D, y_train):
    N = D.shape[0]
    error_counter = 0
    for i in range(N):
        j = np.argmin((D[i]))
        if j == i:
            j = np.argsort(D[i])[1]
        if y_train[j] != y_train[i]:
            error_counter += 1
    return error_counter / N

Nvalues = [100, 200, 400, 800, 1600]
errors = np.zeros((len(Nvalues), 3))
for i, N in enumerate(Nvalues):
    Dinfty = dist_mat(N, d_infty, x_train) #x_train
    D1 = dist_mat(N, d_one, x_train)
    D2 = dist_mat(N, d_two, x_train) 
    
    Erinfty = alg_efficiency(Dinfty, y_train[:N]) #y_train
    Er1 = alg_efficiency(D1, y_train[:N])
    Er2 = alg_efficiency(D2, y_train[:N]) 
    errors[i] = [Erinfty, Er1, Er2]
print("Error Matrix: \n",errors,"\n")

#Plot for first 100 images
N = 100
Dinfty = dist_mat(N, d_infty, x_train)
D1 = dist_mat(N, d_one, x_train)
D2 = dist_mat(N, d_two, x_train)

fig, axs = plt.subplots(1, 3, figsize=(8, 8))
for i, D in enumerate([Dinfty, D1, D2]):
    axs[i].imshow(D)
    axs[i].set_title(f'D{i}' if i > 0 else 'Dinfty')
plt.show()
