import numpy as np
import matplotlib.pyplot as plt
from numba import njit, vectorize
from time import time


@njit
def f(z):
    return z**3 - 1


@njit
def df(z):
    h = 1e-6
    return ((f(z+h) - f(z))/h)

@vectorize(['complex64(complex64, int32)'], target="cuda")
def find_zeros(z, n):
    for i in range(n):
        z -= f(z)/df(z)
    if round(abs(f(z)), 6) == 0:
        return z
    else:
        return np.nan

@vectorize(['complex64(complex64, int32)'], target="cuda")
def newtons_method(z, n):
    for i in range(n):
        z -= f(z)/df(z)
    return z

@njit(parallel=True)
def start_location(matrix, zeros):
    new_matrix = np.zeros((len(matrix), len(matrix)), dtype=np.int32)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[1])):
            for z in range(len(zeros)):
                if matrix[i][j] == zeros[z]:
                    new_matrix[i][j] = z + 1
                    continue
            matrix[i][j] = 0
    return new_matrix
    

@njit
def create_matrix(n):
    matrix = np.zeros((n,n), dtype=np.complex64)
    for x in range(n):
        for y in range(n):
            matrix[y][x] = (complex(x/n*4-2, y/n*4-2))
    return matrix

def plot(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.show()

def main(n):
    #find the zeros of the polynomial
    matrix = create_matrix(100)
    zeros = find_zeros(matrix, 100)
    #create a new and larger matrix
    matrix = create_matrix(n)
    start = time()

    #find the starting location of the zeros using newtons method
    matrix = newtons_method(matrix, 100)

    #round the values to 4 decimals such that we can compare them
    matrix = np.around(matrix, decimals=6)
    zeros = np.around(np.unique(zeros), decimals=6)

    #trace the starting location of the zeros to create colormap of where the zeros originate from.
    matrix = start_location(matrix, zeros)
    end = time()

    print(f"{end - start} seconds to compute newtons fractal")
    plot(matrix)



if __name__ == "__main__":
    main(10000)
