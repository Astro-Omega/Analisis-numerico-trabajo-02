# ======================================
# Insiso N04 por metodo de Punto Falso
# ======================================

from core.machine_falso import punto_falso
from core.misel_met_abierto import crear_funcion, formatear_tabla

funcion_fx = "804.42/x * (1-exp(-0.04878 * x)) - 36"
Xi = 3
Xu = 5
error_permisible = 0.0001

f = crear_funcion(funcion_fx)

try:
    tabla_bis = punto_falso(f, Xi, Xu, error_permisible)
    print(formatear_tabla(tabla_bis).to_string(index=False))
except ValueError as e:
    print(f"error: {e}")