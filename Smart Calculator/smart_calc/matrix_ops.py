import numpy as np
from typing import Tuple


class MatrixOps:
    @staticmethod
    def make_matrix(rows: int, cols: int, flat_list: list) -> np.ndarray:
        arr = np.array(flat_list, dtype=float)
        if arr.size != rows * cols:
            raise ValueError('Number of elements does not match shape')
        return arr.reshape((rows, cols))


    @staticmethod
    def add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        return A + B


    @staticmethod
    def mul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        return A.dot(B)


    @staticmethod
    def transpose(A: np.ndarray) -> np.ndarray:
        return A.T


    @staticmethod
    def det(A: np.ndarray) -> float:
        return float(np.linalg.det(A))


    @staticmethod
    def inv(A: np.ndarray) -> np.ndarray:
        return np.linalg.inv(A)