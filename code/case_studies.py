from typing import List
import numpy as np


def ellipsoid(x: List[float], alpha: int = 1000) -> float:
    d = len(x)
    return sum([np.power(alpha, (i - 1) / (d - 1)) * np.exp2(x[i]) for i in range(d)])
    

def rosenbrock_banana(x1: float, x2: float) -> float:
    return np.exp2(1 - x1) + 100 * np.exp2(x2 - np.power(x1, 2))


def log_ellipsoid(x: List[float], epsilon: float = 1e-4) -> float:
    return np.log(epsilon + ellipsoid(x))


def attractive_sector(x: List[float], q: float = 1e4) -> float:
    d = len(x)
    h = lambda x : np.log(1 + np.exp(q * x)) / q
    return sum([np.exp2(h(x[i])) + 100 * np.exp2(h(x[i])) for i in range(d)])


def sum_of_different_powers_function(x: List[float]) -> float:
    d = len(x)
    return sum([np.power(np.exp2(x[i]), 1 + (i - 1) / (d - 1)) for i in range(d)])

if __name__ == '__main__':
    print("Hello, World!")