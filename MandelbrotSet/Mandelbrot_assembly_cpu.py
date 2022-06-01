import numpy as np
from time import time
from numba import njit
import matplotlib.pyplot as plt


@njit # Using numba to speed up the iterate function
def iterate(c, n):
    """
    Iterate a complex value n times and check if it is in the mandelbrot set
    """
    z = c
    for i in range(n):
        z = z*z + c
        if abs(z) > 2:
            return False  
    return True


def create_matrix(n):
    """
    Create a matrix of complex values ranging from -2 to 2 and -2i to 2i
    """
    x = np.linspace(-2, 2, n)
    y = np.linspace(-2, 2, n)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    return Z
    
@njit # Using numba to speed up the function
def mandelbrot(matrix, iter, n):
    """
    Iterate the complex values in a given n^2 matrix and give set an element's value in bool_matrix to 0 or 1 
    depending on if it is in the mandelbrot set or not.
    """
    bool_matrix = np.zeros((n,n), dtype=np.byte)
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if iterate(matrix[x][y], iter):
                bool_matrix[x][y] = 1
            else:
                bool_matrix[x][y] = 0
    return bool_matrix

def plot(matrix):
    """
    Plot the matrix containing boolean values for the mandelbrot set using matplotlib.
    """
    plt.imshow(matrix, cmap='binary')
    plt.show()



def main():
    n = 1000
    start = time()
    matrix = create_matrix(n)
    print(f"Matrix created in: {time() - start} seconds")
    start = time()
    matrix = mandelbrot(matrix, 100, n)
    print(f"Iterating through the grid took: {time() - start} seconds")
    print(f"number of operations required was {(n**2*100)/1e9} * 10 ^ 9")
    plot(matrix)

if __name__ == "__main__":
    main()
