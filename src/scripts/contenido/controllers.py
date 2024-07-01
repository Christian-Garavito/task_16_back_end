from flask import request
import psycopg2
from .queries import Query
from .manejo_grafos import encontrar_ruta_optima


# ------------------------------tabla vuelos---------------------
# ----------------------1. obtener el contenido de la tabla vuelos-----------------
def obtener_vuelos():
    try:
        entrada = request.args
        origen = entrada["origen"]
        destino = entrada["destino"]
        fecha = entrada["fecha"]
        orden = entrada["orden"]

        if origen == destino:
            raise ValueError("El Origen debe ser diferente al destino")



    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    try:
        # Obtener vuelos desde la base de datos filtrando por fecha
        results = Query().buscar_tabla_vuelos(fecha)

        # Encontrar ruta óptima según el orden especificado
        ruta_optima = encontrar_ruta_optima(results, origen, destino, orden)

        if ruta_optima:
            return {
                "msg": f"Ruta óptima encontrada según {orden}",
                "codigo": 1,
                "status": True,
                "obj": {"ruta_optima": ruta_optima},
            }
        else:
            return {
                "msg": f"No se encontró ruta óptima según {orden}",
                "codigo": 2,
                "status": False,
                "obj": {},
            }

    except psycopg2.Error as db_error:
        return {
            "msg": f"Error de base de datos: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}


# ------------------------------tabla vuelos---------------------
# ----------------------------crud vuelos-----------------------------
def crud_vuelos(pk_id_vuelo=None):
    if request.method == "GET":
        return obtener_vuelos()
