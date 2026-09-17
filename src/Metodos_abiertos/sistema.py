"""
Método de Newton-Raphson para sistemas no lineales 2x2 - Inciso N03
"""


def newton_raphson_sistema(F1, F2, J, x0, y0, tol=1e-4, max_iter=100):
    """
    F1, F2 : funciones del sistema F(x,y) = 0
    J      : función que retorna (a, b, c, d) = (dF1/dx, dF1/dy, dF2/dx, dF2/dy)
    """
    print(f"{'i':>3} {'xi':>12} {'yi':>12} {'F1':>12} {'F2':>12} {'x(n+1)':>12} {'y(n+1)':>12}")
    xi, yi = x0, y0
    for i in range(1, max_iter + 1):
        f1 = F1(xi, yi)
        f2 = F2(xi, yi)
        a, b, c, d = J(xi, yi)
        det = a * d - b * c
        if det == 0:
            print("det(J) = 0 -> el método falla.")
            return None
        dx = (d * f1 - b * f2) / det
        dy = (-c * f1 + a * f2) / det
        x1 = xi - dx
        y1 = yi - dy
        print(f"{i:>3} {xi:>12.6f} {yi:>12.6f} {f1:>12.6f} {f2:>12.6f} {x1:>12.6f} {y1:>12.6f}")
        if abs(x1 - xi) < tol and abs(y1 - yi) < tol:
            return x1, y1
        xi, yi = x1, y1
    return xi, yi


if __name__ == "__main__":

    # --- Inciso N03: sistema no lineal ---
    # F1: -x^2 + x + 0.75 - y = 0
    # F2:  y + 5xy - x^2 = 0
    print("=== INCISO N03 - Newton-Raphson (sistema 2x2) ===")
    F1 = lambda x, y: -(x ** 2) + x + 0.75 - y
    F2 = lambda x, y: y + 5 * x * y - x ** 2
    J = lambda x, y: (1 - 2 * x, -1, 5 * y - 2 * x, 1 + 5 * x)   # (a, b, c, d)
    newton_raphson_sistema(F1, F2, J, x0=1.3, y0=0.2, tol=1e-4, max_iter=4)
