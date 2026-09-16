import pandas as pd

def biseccion(f, Xi, Xu, error_permisible, max_iter=50):
    if f(Xi) * f(Xu) > 0:
        raise ValueError("f(Xi)*f(Xu) > 0: no se garantiza una raíz en el intervalo dado.")

    filas = []

    for i in range(0, max_iter + 1):
        Xr = (Xi + Xu) / 2
        f_Xi, f_Xu, f_Xr = f(Xi), f(Xu), f(Xr)
        producto_Xi_Xu = f_Xi * f_Xu
        producto_Xi_Xr = f_Xi * f_Xr

        error = abs((Xr - Xu) / Xr) 

        filas.append({
            "i": i, "Xi": Xi, "Xu": Xu,
            "F(Xi)": f_Xi, "F(Xu)": f_Xu, "F(Xi)*F(Xu)": producto_Xi_Xu,
            "Xr": Xr, "F(Xr)": f_Xr, "F(Xi)*F(Xr)": producto_Xi_Xr,
            "Error": error
        })

        if error is not None and error < error_permisible:
            break

        if producto_Xi_Xr < 0:
            Xu = Xr
        elif producto_Xi_Xr > 0:
            Xi = Xr
        else:
            break

    return pd.DataFrame(filas)