""" Controladores del servicio 1 """



from flask import request
import psycopg2


from .queries import Query
from .clase_ejemplo import ClaseEjemplo


#------------------------------tabla_contenido_imdb---------------------
#----------------------1. obtener el contenido de la tabla-----------------
def obtener_contenidos():
    try:
        # datos como un diccionario
        # metodo tiene limites aplicarlos el metodo get no resive booy por eso se usa el args
        
        entrada = request.args
        print("--------------------------------------------------")   
        print(entrada)
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    try:
        results,hay_siguiente = Query().buscar_contenidos(entrada)
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

#------------------------------tabla_contenido_imdb---------------------
#-----------------------------------2. agregar contenido---------------------
def agregar_contenidos():
    try:
        # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_contenido(entrada.get("pk_id_peliculas"), entrada.get("titulo_pelicula"), entrada.get("ano_pelicula"),entrada.get("fk_id_tipo_contenido"),entrada.get("director_pelicula"),entrada.get("valor_pelicula"))
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
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla_contenido_imdb---------------------
#-----------------------------------3. editar contenido---------------------
def editar_contenidos(pk_id_peliculas):
    try:
         # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().editar_contenido(pk_id_peliculas, entrada.get("titulo_pelicula"), entrada.get("ano_pelicula"),entrada.get("fk_id_tipo_contenido"),entrada.get("director_pelicula"),entrada.get("valor_pelicula"))
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
        "msg": "contenido editado satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla_contenido_imdb---------------------
#----------------------------cued contenido-----------------------------
def crud_contenido(pk_id_peliculas=None):
    if request.method == "GET":
        return obtener_contenidos()
    if request.method == "POST":
        return agregar_contenidos()
    if request.method == "PUT":
        return editar_contenidos(pk_id_peliculas)
    


#------------------------------tabla tipo_contenido---------------------
#1. obtener tipo_contenido---------------------------------------------------
def obtener_tipo_contenidos():
    try:
        # datos como un diccionario
        entrada = request.args
        #print(entrada)
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    try:
        results = Query().buscar_tipo_contenido(entrada)
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
        "obj": results,
    }

#------------------------------tabla tipo_contenido---------------------
#2. agregar  tipo_contenido------------------------------------------------
def agregar_tipo_contenidos():
    try:
        # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_tipo_contenido(entrada.get("pk_id_tipo_contenido"), entrada.get("tipo_contenido"), entrada.get("decripcion_contenido"),entrada.get("valor_generado"))
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
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla tipo_contenido---------------------
#3. editar tipo_contenido---------------------------------------------------
def editar_tipo_contenidos(pk_id_tipo_contenido):
    try:
         # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().editar_tipo_contenido(pk_id_tipo_contenido, entrada.get("tipo_contenido"), entrada.get("decripcion_contenido"),entrada.get("valor_generado"))
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
        "msg": "contenido editado satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla tipo_contenido---------------------
#cued tipo_contenido-----------------------------------------------------
def crud_tipo_contenido(pk_id_tipo_contenido=None):
    if request.method == "GET":
        return obtener_tipo_contenidos()
    if request.method == "POST":
        return agregar_tipo_contenidos()
    if request.method == "PUT":
        return editar_tipo_contenidos(pk_id_tipo_contenido)




#------------------------------tabla tabla_generos---------------------
#1. obtener tabla_generos---------------------------------------------------
def obtener_tabla_generos():
    try:
        # datos como un diccionario
        entrada = request.args
        #print(entrada)
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    try:
        results = Query().buscar_tabla_generos(entrada)
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
        "obj": results,
    }

#------------------------------tabla tabla_generos---------------------
#2. agregar  tabla_generos------------------------------------------------
def agregar_tabla_generos():
    try:
        # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_tabla_genero(entrada.get("pk_genero"), entrada.get("nombre_genero"), entrada.get("descripcion_genero"))
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
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla tabla_generos---------------------
#3. editar tipo_contenido---------------------------------------------------
def editar_tabla_generos(pk_genero):
    try:
         # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().editar_tabla_genero(pk_genero, entrada.get("nombre_genero"), entrada.get("descripcion_genero"))
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
        "msg": "contenido editado satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla tabla_generos---------------------
#cued tabla_generos-----------------------------------------------------
def crud_tabla_generos(pk_genero=None):
    if request.method == "GET":
        return obtener_tabla_generos()
    if request.method == "POST":
        return agregar_tabla_generos()
    if request.method == "PUT":
        return editar_tabla_generos(pk_genero)





#------------------------------tabla union_peliculas_generos---------------------
#1. obtener union_peliculas_generos---------------------------------------------------
def obtener_union_peliculas_generos():
    try:
        results = Query().buscar_union_peliculas_generos()
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
        "obj": results,
    }

#------------------------------tabla union_peliculas_generos---------------------
#2. agregar  union_peliculas_generos------------------------------------------------
def agregar_union_peliculas_generos():
    try:
        # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_union_peliculas_genero(entrada.get("pk_id_peliculas"), entrada.get("pk_genero"))
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
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla union_peliculas_generos---------------------
#cued union_peliculas_generos-----------------------------------------------------
def crud_union_peliculas_generos():
    if request.method == "GET":
        return obtener_union_peliculas_generos()
    if request.method == "POST":
        return agregar_union_peliculas_generos()








