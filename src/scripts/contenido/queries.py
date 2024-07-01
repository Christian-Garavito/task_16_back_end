""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # ------------------------tabla de vuelos------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    # filtros
    def buscar_tabla_vuelos(self, fecha):
        """
        It does nothing.
        """

        query = f"""SELECT vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida 
                FROM public.tabla_vuelos WHERE hora_salida >= '{fecha}'"""


        print(query)
        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                columnas = [columna.name for columna in cursor.description or []]

                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                return objeto_contenidos
