import pandas as pd

def punto_falso(f, Xi, Xu, error_permisible, max_iter=50):
    if f(Xi) * f(Xu) > 0:
        raise ValueError("f(Xi)*f(Xu) > 0: no se garantiza una raíz en el intervalo dado.")

    filas = []
    Xr_anterior = None

    for i in range(0, max_iter + 1):
        f_Xi, f_Xu = f(Xi), f(Xu)
        Xr = Xu - (f_Xu * (Xi - Xu)) / (f_Xi - f_Xu)
        f_Xr = f(Xr)

        error = None if Xr_anterior is None else abs((Xr - Xr_anterior) / Xr)

        filas.append({
            "i": i, "Xi": Xi, "Xu": Xu, "Xr": Xr,
            "f(Xi)": f_Xi, "f(Xu)": f_Xu, "f(Xr)": f_Xr,
            "Error": error
        })

        if error is not None and error < error_permisible:
            break

        if f_Xi * f_Xr < 0:
            Xu = Xr
        elif f_Xi * f_Xr > 0:
            Xi = Xr
        else:
            break

        Xr_anterior = Xr

    return pd.DataFrame(filas)



