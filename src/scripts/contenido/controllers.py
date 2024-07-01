""" Controladores del servicio 1 """
from flask import request
import psycopg2
from .queries import Query
from .clase_ejemplo import ClaseEjemplo


#------------------------------tabla vuelos---------------------
#----------------------1. obtener el contenido de la tabla vuelos-----------------
def obtener_vuelos():
    try:
        # datos como un diccionario
        # metodo tiene limites aplicarlos el metodo get no resive booy por eso se usa el args
        
        entrada = request.args
        print("--------------------------------------------------")   
        print(entrada)
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    try:
        results,hay_siguiente = Query().buscar_tabla_vuelos(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": {"results" : results, "hay_sigiente": hay_siguiente},
        
    }
#------------------------------tabla vuelos---------------------
#----------------------------cued vuelos-----------------------------
def crud_vuelos(pk_id_vuelo=None):
    if request.method == "GET":
        return obtener_vuelos()
   
    
