import numpy as np

from petro_props.real_gas.kay_mixing import calculate_critical_props
from petro_props.real_gas.hall_yarborough import calculate_Z


def _calculate_M(y: np.ndarray, mw: np.ndarray) -> np.ndarray:
    return np.sum(y * mw)


def calculate_density(
    T: float, p: float, mw: np.ndarray, T_c: np.ndarray, p_c: np.ndarray, y: np.ndarray
) -> float:
    M = _calculate_M(y, mw)
    T_pc, p_pc = calculate_critical_props(y, T_c, p_c)
    Z = calculate_Z(T / T_pc, p / p_pc)
    R = 8.314
    return p * M / (Z * R * T)
