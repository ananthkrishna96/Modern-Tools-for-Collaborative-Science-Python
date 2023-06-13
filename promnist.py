import timeit
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import interpolate
from scipy import integrate

%pylab inline

arc = load('mnist.npz')

x_train = arc['arr_0']
y_train = arc['arr_1']
x_test  = arc['arr_2']
y_test  = arc['arr_3']

#print(x_train.shape, y_train.shape)
#print(x_test.shape, y_test.shape)

#Distance between Images

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

#Compute for first 100 images
N = 100
Dinfty = dist_mat(N, d_infty, x_train)
D1 = dist_mat(N, d_one, x_train)
D2 = dist_mat(N, d_two, x_train)

fig, axs = plt.subplots(1, 3, figsize=(8, 8))
for i, D in enumerate([Dinfty, D1, D2]):
    axs[i].imshow(D)
    axs[i].set_title(f'D{i}' if i > 0 else 'Dinfty')
plt.show()
