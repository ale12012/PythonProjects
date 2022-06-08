import matplotlib.pyplot as plt
import numpy as np
from numba import vectorize, njit
import numba
from time import time


""""
This function creates a matrix of complex numbers from -2 to 2 and -2i to 2i
    Args:
        n: dimention of the matrix
    Returns:
        matrix: matrix of complex numbers
"""
@njit
def create_matrix(n):
    matrix = np.zeros((n,n), dtype=np.complex64)
    for x in range(n):
        for y in range(n):
            matrix[y][x] = (complex(x/n*4-2, y/n*4-2))
    return matrix


"""
This function takes a complex number and iterates it n times with the formula z = z*z + c 
and returns the number of iterations it took for the absolute value of the complex number to become larger than 2.
    Args:
        z: element of the matrix
        n: number of times to iterate
    Returns:
        i: number between 0 and n
"""
@vectorize(['int32(complex64, int32)'], target="cuda")
def iterate(z, n):
    c = z
    for i in range(n):
        z = z*z + c
        if abs(z) > 2:
            return i
    return i


"""
This function creates a heatmap of a given 2d matrix
    Args:
        matrix: matrix to be plotted
    Output:
        heatmap: heatmap of the matrix with a random colorscheme in matplotlib's pyplot
"""
def plot(matrix):
    colors = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    random_color = np.random.choice(colors)
    plt.imshow(matrix, cmap=f'{random_color}')
    plt.show()



"""
Main function where you can alter the number of iterations and the size of the matrix
"""
def main():
    time_start = time()
    #create a matrix of complex numbers with dimention n^2
    matrix = create_matrix(20000)
    #benchmark
    print(f"Time taken to crate the matrix: {time() - time_start} seconds")
    time_start = time()
    #iterate the matrix using gpu
    matrix = iterate(matrix, 300)

    #benchmark results
    print(f"Time taken to iterate through the matrix: {time() - time_start} seconds")
    plot(matrix)

if __name__ == '__main__':
    main()
     