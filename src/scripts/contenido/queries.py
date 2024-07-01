""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # ------------------------tabla de vuelos------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_tabla_vuelos(self, filtros):
        """
        It does nothing.
        """
    

        query = "SELECT x.* FROM public.tabla_vuelos x"
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if filtros:
            print(f"Filtros:{filtros}")
            condiciones = []
            for columna, valor in filtros.items():
                if columna == "pagina":
                    pagina = valor
                    # print(pagina)
                elif columna == "limit":
                    limit = valor
                else:
                    condiciones.append(f"{columna} = '{valor}'")

            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)

        
        # ordenar la tabla
        query += " ORDER BY pk_id_vuelo"
        print(query)

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                # print(response)
                # print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

       
                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                # print(objeto_contenidos)

                return objeto_contenidos
