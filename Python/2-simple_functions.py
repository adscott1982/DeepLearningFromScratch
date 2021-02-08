import numpy as np


def square(x: np.ndarray) -> np.ndarray:
    """ Square each element in the input ndarray. """
    return np.power(x, 2)


def leaky_relu(x: np.ndarray) -> np.ndarray:
    """ Apply "Leaky ReLU" function to each element in ndarray. """
    return np.maximum(0.2 * x, x)


print(f'4 squared = {square(4)}')




