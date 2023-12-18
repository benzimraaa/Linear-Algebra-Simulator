import numpy as np
from colorama import Fore, Style


# Function to print matrix in color
def print_colored_matrix(matrix):
    if matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    for row in matrix:
        for element in row:
            if element >= 0:
                print(Fore.GREEN + f"{element}, ", end="")
            else:
                print(Fore.RED + f"{element} ", end="")
        print(Style.RESET_ALL)  # Reset color after each row