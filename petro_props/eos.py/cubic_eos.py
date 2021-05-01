import numpy as np
from typing import Dict
from dataclasses import dataclass
import pandas as pd

R = 8.314


@dataclass
class EosProps:
    mw: float
    pc: float
    Tc: float
    af: float


class CubicEos:
    def __init__(
        self,
        Omega_a: float,
        Omega_b: float,
        properties: Dict[str, EosProps],
        bips: pd.DataFrame,
    ):
        self.Omega_a = Omega_a
        self.Omega_b = Omega_b
        self.properties = properties
        self.bips = bips

    def calculate_p(self, T: float, v: float, z: np.ndarray) -> float:
        a = self._calculate_a(T, z)
        b = self._calculate_b(T, z)
        return R * T / (v - b) - a / self._D(v, b)

    def _calculate_a(self, T: float, z: np.ndarray) -> float:
        ai = np.zeros_like((self.properties.keys()))
        alpha = self._calculate_alpha(T)
        for i, comp in enumerate(self.properties.keys()):
            Tc = self.properties[comp].Tc
            pc = self.properties[comp].pc
            ai[i] = self.Omega_a * R ** 2 * Tc ** 2 / pc * alpha

    def _calculate_b(self, T: float, z: np.ndarray) -> float:
        bi = {}
        for comp in self.properties.keys():
            Tc = self.properties[comp].Tc
            pc = self.properties[comp].pc
            bi[comp] = self.Omega_a * R * Tc / pc

    def _calculate_alpha(self, T: float) -> float:
        pass

    def _D(self, v: float, b: float) -> float:
        pass
