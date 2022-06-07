import numpy as np
import matplotlib.pyplot as plt
from numba import njit, vectorize
from time import time


@njit
def f(z):
    return z**2 - 3*z + 13


@njit
def df(z):
    h = 1e-6
    return ((f(z+h) - f(z))/h)

@vectorize(['complex64(complex64, int32)'], target="cuda")
def find_zeros(z, n):
    for i in range(n):
        z -= f(z)/df(z)
    if round(abs(f(z)), 5) == 0:
        return z
    else:
        return np.nan


@njit
def create_matrix(n):
    matrix = np.zeros((n,n), dtype=np.complex64)
    for x in range(n):
        for y in range(n):
            matrix[y][x] = (complex(x/n*4-2, y/n*4-2))
    return matrix


def main(n):
    matrix = create_matrix(n)
    start = time()
    zeros = find_zeros(matrix, 100)
    end = time()
    print(end - start)
    print(np.unique(np.around(zeros, decimals=5)))


if __name__ == "__main__":
    main(100)
