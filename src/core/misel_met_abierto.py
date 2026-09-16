import sympy as sp
import pandas as pd

x = sp.symbols('x')

def crear_funcion(funcion_str):
    f_expr = sp.sympify(funcion_str)
    return sp.lambdify(x, f_expr, 'numpy')

def formatear_tabla(tabla):
    tabla_fmt = tabla.copy()
    tabla_fmt["Error"] = tabla_fmt["Error"].apply(
        lambda v: "" if pd.isna(v) else f"{v:.6f}"
    )
    for col in tabla_fmt.columns:
        if col not in ("i", "Error"):
            tabla_fmt[col] = tabla_fmt[col].apply(lambda v: f"{v:.6f}")
    return tabla_fmt