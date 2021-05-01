from typing import Tuple
import numpy as np


def calculate_critical_props(
    y: np.ndarray, T_c: np.ndarray, p_c: np.ndarray
) -> Tuple[float, float]:
    T_pc = np.sum(y * T_c)
    p_pc = np.sum(y * p_c)
    return T_pc, p_pc
