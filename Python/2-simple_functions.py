import numpy as np
from typing import Callable
from numpy import ndarray


def square(x: ndarray) -> ndarray:
    """ Square each element in the input ndarray. """
    return np.power(x, 2)


def leaky_relu(x: ndarray) -> ndarray:
    """ Apply "Leaky ReLU" function to each element in ndarray. """
    return np.maximum(0.2 * x, x)


def derivative(func: Callable[[ndarray], ndarray],
               input_: ndarray,
               delta: float = 0.001) -> ndarray:
    """ Evaluates the derivative of a function "func" at every element in the "input" array"""
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


print(f'Derivative of square of 2 = {derivative(square, 2, 0.1)}')
