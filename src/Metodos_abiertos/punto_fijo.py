"""
Método de Punto Fijo - Inciso N01 e Inciso N03
"""

import math


def punto_fijo(g, x0, tol=1e-4, max_iter=100):
    """
    xi+1 = g(xi)
    g   : función de iteración
    x0  : valor inicial
    tol : error aproximado permisible (Ea)
    """
    print(f"{'i':>3} {'Xi':>12} {'Xi+1':>12} {'Ea(%)':>12}")
    xi = x0
    for i in range(1, max_iter + 1):
        xi1 = g(xi)
        ea = abs((xi1 - xi) / xi1) * 100
        print(f"{i:>3} {xi:>12.6f} {xi1:>12.6f} {ea:>12.6f}")
        if ea < tol * 100:
            return xi1
        xi = xi1
    return xi


if __name__ == "__main__":

    # --- Inciso N01: g(x) = sin(sqrt(x)), X0 = 0.5 ---
    print("=== INCISO N01 - Punto Fijo ===")
    g1 = lambda x: math.sin(math.sqrt(x))
    punto_fijo(g1, x0=0.5, tol=1e-4)

    # --- Inciso N03: sistema no lineal resuelto por sustitución (punto fijo) ---
    # F1: -x^2 + x + 0.75 - y = 0  ->  x = (1 + 2*sqrt(1-y)) / 2
    # F2:  y + 5xy - x^2 = 0       ->  y = x^2 / (1 + 5x)
    print("\n=== INCISO N03 - Punto Fijo (sistema) ===")
    g_y = lambda x: (x ** 2) / (1 + 5 * x)
    g_x = lambda y: (1 + 2 * math.sqrt(1 - y)) / 2

    xi = 1.2
    print(f"{'i':>3} {'Xi':>12} {'y':>12} {'Xi+1':>12} {'Ea(%)':>12}")
    for i in range(1, 7):
        yi = g_y(xi)
        xi1 = g_x(yi)
        ea = abs((xi1 - xi) / xi1) * 100
        print(f"{i:>3} {xi:>12.6f} {yi:>12.6f} {xi1:>12.6f} {ea:>12.6f}")
        xi = xi1
