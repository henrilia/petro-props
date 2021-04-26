import numpy as np


def _calculate_theta(T_pr: float) -> float:
    return 1 / T_pr


def _calculate_alpha(theta: float) -> float:
    return 0.06125 * theta * np.exp(-1.2 * (1 - theta) ** 2)


def _f1(rho_hat: float, alpha: float, p_pr: float) -> float:
    return (
        -alpha * p_pr
        + (rho_hat + rho_hat ** 2 + rho_hat ** 3 - rho_hat ** 4) / (1 - rho_hat) ** 3
    )


def _f2(rho_hat: float, theta: float) -> float:
    return -(14.76 * theta - 9.76 * theta ** 2 + 4.58 * theta ** 3) * rho_hat ** 2


def _f3(rho_hat: float, theta: float) -> float:
    return (90.7 * theta - 242.2 * theta ** 2 + 42.4 * theta ** 3) * rho_hat ** (
        2.18 + 2.82 * theta
    )


def _f(rho_hat: float, theta: float, alpha: float, p_pr: float) -> float:
    return _f1(rho_hat, alpha, p_pr) + _f2(rho_hat, theta) + _f3(rho_hat, theta)


def _fp1(rho_hat: float, alpha: float, p_pr: float) -> float:
    return (1 + 4 * rho_hat + 4 * rho_hat ** 2 - 4 * rho_hat ** 3 + rho_hat ** 4) / (
        1 - rho_hat
    ) ** 4


def _fp2(rho_hat: float, theta: float) -> float:
    return -(29.52 * theta - 19.52 * theta ** 2 + 9.16 * theta ** 3) * rho_hat


def _fp3(rho_hat: float, theta: float) -> float:
    return (
        (2.18 + 2.82 * theta)
        * (90.7 * theta - 242.2 * theta ** 2 + 42.4 * theta ** 3)
        * rho_hat ** (1.18 + 2.82 * theta)
    )


def _fp(rho_hat: float, theta: float, alpha: float, p_pr: float) -> float:
    return _fp1(rho_hat, alpha, p_pr) + _fp2(rho_hat, theta) + _fp3(rho_hat, theta)


def _calculate_rho_hat(theta: float, alpha: float, p_pr: float) -> float:
    xn = 0.1
    for n in range(0, 200):
        fxn = -_f(xn, theta, alpha, p_pr)
        if np.abs(fxn) < 0.01:
            return xn
        fpxn = _fp(xn, theta, alpha, p_pr)
        if fpxn == 0:
            return None
        xn = xn - fxn / fpxn
    return None


def calculate_Z(T_pr: float, p_pr: float) -> float:
    theta = _calculate_theta(T_pr)
    alpha = _calculate_alpha(theta)
    rho_hat = _calculate_rho_hat(theta, alpha, p_pr)
    return alpha * p_pr / rho_hat


__all__ = [calculate_Z]
