import matplotlib.pyplot as plt
import numpy as np
from numba import vectorize, njit
import numba
from time import time

@njit
def create_matrix(n):
    matrix = np.zeros((n,n), dtype=np.complex64)
    for x in range(n):
        for y in range(n):
            matrix[y][x] = (complex(x/n*4-2, y/n*4-2))
    return matrix


#create a function that takes an element of the matrix and returns and iterates it n times with the formula z = z*z + c just like in the mandelbrot set
@vectorize(['int32(complex64, int32)'], target="cuda")
def iterate(z, n):
    c = z
    for i in range(n):
        z = z*z + c
        if abs(z) > 2:
            return i
    return i



def plot(matrix):
    colors = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    random_color = np.random.choice(colors)
    plt.imshow(matrix, cmap=f'{random_color}')
    plt.show()

def main():
    time_start = time()
    #create a matrix of complex numbers
    matrix = create_matrix(5000)
    #benchmark
    print(f"Time taken to crate the matrix: {time() - time_start} seconds")
    time_start = time()
    #iterate the matrix using gpu
    matrix = iterate(matrix, 200)

    #benchmark results
    print(f"Time taken to iterate through the matrix: {time() - time_start} seconds")
    plot(matrix)

if __name__ == '__main__':
    main()
     