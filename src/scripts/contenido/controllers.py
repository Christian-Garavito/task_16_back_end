from flask import request
import psycopg2
from .queries import Query
from .manejo_grafos import encontrar_ruta_optima_dijkstra


# ------------------------------tabla vuelos---------------------
# ----------------------1. obtener el contenido de la tabla vuelos-----------------
def obtener_vuelos():
    try:
         # Obtener los parámetros de la solicitud
        entrada = request.args 
        # Obtener el parámetro 'origen'
        origen = entrada["origen"]
        # Obtener el parámetro 'destino'  
        destino = entrada["destino"]
        # Obtener el parámetro 'fecha'  
        fecha = entrada["fecha"]
        # Obtener el parámetro 'orden'  
        orden = entrada["orden"]
         # Obtener el parámetro 'escalas' y convertirlo a entero  
        escalas = int( entrada["escalas"] ) 

        # Verificar si el origen y destino son iguales
        if origen == destino:  
            # Lanzar un error si son iguales
            raise ValueError(
                "El Origen debe ser diferente al destino"
            )  

    except Exception as exc:
        return {
            "msg": str(exc),
            "codigo": 0,
            "status": False,
            "obj": {},
        }  

    try:
        # Obtener vuelos desde la base de datos filtrando por fecha
        results = Query().buscar_tabla_vuelos(fecha)

        # Encontrar ruta óptima según el orden especificado
        ruta_optima = encontrar_ruta_optima_dijkstra( results, origen, destino, orden, escalas)
        
        # Verificar si se encontró una ruta óptima
        if ruta_optima[0]:  
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
    # Manejar errores de la base de datos
    except psycopg2.Error as db_error:
        return {
            "msg": f"Error de base de datos: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        } 
    # Manejar otros errores 
    except Exception as exc:
        return {
            "msg": str(exc),
            "codigo": 0,
            "status": False,
            "obj": {},
        }  


# ------------------------------tabla vuelos---------------------
# ----------------------------crud vuelos-----------------------------
 # Llamar a la función obtener_vuelos() si el método de la solicitud es GET
def crud_vuelos(pk_id_vuelo=None):
    if request.method == "GET":
        return (
            obtener_vuelos()
        ) 
