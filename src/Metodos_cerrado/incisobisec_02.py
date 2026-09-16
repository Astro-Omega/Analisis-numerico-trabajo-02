# ======================================
# Insiso N02 por metodo de Bisectris
# ======================================

from core.machine_biseccion import biseccion
from core.misel_met_abierto import crear_funcion, formatear_tabla

funcion_fx = "tan(x) + exp(-x)"
Xi = 2
Xu = 4
error_permisible = 0.0001

f = crear_funcion(funcion_fx)

try:
    tabla_bis = biseccion(f, Xi, Xu, error_permisible)
    print(formatear_tabla(tabla_bis).to_string(index=False))
except ValueError as e:
    print(f"error: {e}")
