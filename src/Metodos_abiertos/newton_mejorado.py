"""
Método de Newton-Raphson Mejorado - Inciso N02
"""

import math


def newton_raphson_mejorado(f, df, d2f, x0, tol=1e-4, max_iter=100):
    """
    xi+1 = xi - [f(xi)*f'(xi)] / [ (f'(xi))^2 - f(xi)*f''(xi) ]
    """
    print(f"{'i':>3} {'Xi':>14} {'f(xi)':>14} {'f\'(xi)':>14} {'f\'\'(xi)':>14} {'xi+1':>14} {'Error':>12}")
    xi = x0
    for i in range(1, max_iter + 1):
        fxi = f(xi)
        dfxi = df(xi)
        d2fxi = d2f(xi)
        denom = dfxi ** 2 - fxi * d2fxi
        if denom == 0:
            print("Denominador = 0 -> el método falla.")
            return None
        xi1 = xi - (fxi * dfxi) / denom
        err = abs((xi1 - xi) / xi1) if xi1 != 0 else abs(xi1 - xi)
        print(f"{i:>3} {xi:>14.6f} {fxi:>14.6f} {dfxi:>14.6f} {d2fxi:>14.6f} {xi1:>14.6f} {err:>12.8f}")
        if err < tol:
            return xi1
        xi = xi1
    return xi


if __name__ == "__main__":

    # --- Inciso N02: f(x) = e^(-0.5x)*(4-x) - 2 ---
    f2 = lambda x: math.exp(-0.5 * x) * (4 - x) - 2
    df2 = lambda x: -0.5 * math.exp(-0.5 * x) * (4 - x) - math.exp(-0.5 * x)
    d2f2 = lambda x: 0.25 * math.exp(-0.5 * x) * (4 - x) + 0.5 * math.exp(-0.5 * x) + 0.5 * math.exp(-0.5 * x)

    for x0 in (2, 6, 8):
        print(f"=== INCISO N02 - Newton-Raphson Mejorado (X0={x0}) ===")
        newton_raphson_mejorado(f2, df2, d2f2, x0=x0, tol=1e-4, max_iter=6)
        print()
