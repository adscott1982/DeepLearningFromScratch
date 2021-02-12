from typing import Callable
from typing import List
import numpy as np
from numpy import ndarray

# A function takes in an ndarray as an argument and produced an ndarray
Array_Function = Callable[[ndarray], ndarray]

# A Chain is a list of functions
Chain = List[Array_Function]


def chain_length_2(chain: Chain,
                   x: ndarray) -> ndarray:
    """ Evaluates two functions in a row, in a "Chain". """

    assert len(chain) == 2, \
        "Length of input 'chain' should be 2"

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(x))


def square(x: ndarray) -> ndarray:
    """ Square each element in the input ndarray. """
    return np.power(x, 2)


Array_Function = square
chain1 = [square, square]

print(f"2 squared then squared = {chain_length_2(chain1, 2)}")

