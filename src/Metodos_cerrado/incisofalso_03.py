# ======================================
# Insiso N03 por metodo de Punto Falso
# ======================================

from core.machine_falso import punto_falso
from core.misel_met_abierto import crear_funcion, formatear_tabla

funcion_fx = "atan(x) + x - 1"
Xi = 0
Xu = 1
error_permisible = 0.0001

f = crear_funcion(funcion_fx)

try:
    tabla_bis = punto_falso(f, Xi, Xu, error_permisible)
    print(formatear_tabla(tabla_bis).to_string(index=False))
except ValueError as e:
    print(f"error: {e}")