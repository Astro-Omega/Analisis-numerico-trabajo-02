"""
Método de Newton-Raphson - Inciso N01 e Inciso N02
"""

import math


def newton_raphson(f, df, x0, tol=1e-4, max_iter=100):
    """
    xi+1 = xi - f(xi)/f'(xi)
    """
    print(f"{'i':>3} {'Xi':>14} {'f(xi)':>14} {'f\'(xi)':>14} {'xi+1':>14} {'Ea(%)':>12}")
    xi = x0
    for i in range(1, max_iter + 1):
        fxi = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            print("f'(xi) = 0 -> el método falla (tangente horizontal).")
            return None
        xi1 = xi - fxi / dfxi
        ea = abs((xi1 - xi) / xi1) * 100
        print(f"{i:>3} {xi:>14.6f} {fxi:>14.6f} {dfxi:>14.6f} {xi1:>14.6f} {ea:>12.6f}")
        if ea < tol * 100:
            return xi1
        xi = xi1
    return xi


if __name__ == "__main__":

    # --- Inciso N01: f(x) = sin(sqrt(x)) - x, X0 = 0.5 ---
    print("=== INCISO N01 - Newton-Raphson ===")
    f1 = lambda x: math.sin(math.sqrt(x)) - x
    df1 = lambda x: math.cos(math.sqrt(x)) / (2 * math.sqrt(x)) - 1
    newton_raphson(f1, df1, x0=0.5, tol=1e-4)

    # --- Inciso N02: f(x) = e^(-0.5x)*(4-x) - 2 ---
    f2 = lambda x: math.exp(-0.5 * x) * (4 - x) - 2
    df2 = lambda x: -0.5 * math.exp(-0.5 * x) * (4 - x) - math.exp(-0.5 * x)

    for x0 in (2, 6, 8):
        print(f"\n=== INCISO N02 - Newton-Raphson (X0={x0}) ===")
        newton_raphson(f2, df2, x0=x0, tol=1e-4, max_iter=5)
