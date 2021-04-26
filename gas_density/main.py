import numpy as np


def calculate_rho(T: float, p: float, Z: float, M: float) -> float:
    R = 8.314
    return p * M / (Z * R * T)


def calculate_M(y: np.ndarray, mw: np.ndarray) -> np.ndarray:
    return np.sum(y * mw)


if __name__ == "__main__":
    from gas_density.read_input import read_composition_and_props
    from gas_density.kay_mixing import calculate_critical_props
    from gas_density.hall_yarborough import calculate_Z

    T = float(input("T [degC] = ")) + 273
    p = float(input("p [bar] = "))
    filepath = input("path to excel input = ")
    mw, T_c, p_c, y = read_composition_and_props(filepath)
    M = calculate_M(y, mw)
    T_pc, p_pc = calculate_critical_props(y, T_c, p_c)
    Z = calculate_Z(T / T_pc, p / p_pc)
    rho = calculate_rho(T, p, Z, M)
    print(f"Density = {rho}")
