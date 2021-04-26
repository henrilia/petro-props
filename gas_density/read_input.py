from typing import Tuple
import pandas as pd
import numpy as np


def read_composition_and_props(
    filepath: str,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Read an excel sheet where columns from left to right is:
        Component name
        Molecular weight
        Critical pressure
        Critical temperature
        Molar precentage

    Molecular weight in mole/g, pressure in bar and temperature in K
    """
    df = pd.read_excel(filepath)
    mw = df.iloc[:, 1].to_numpy()
    p_c = df.iloc[:, 2].to_numpy()
    T_c = df.iloc[:, 3].to_numpy()
    y = df.iloc[:, 4].to_numpy() / 100
    return mw, T_c, p_c, y
