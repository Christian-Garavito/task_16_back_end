""" Queries del servicio 1 """

from src.scripts.connection import Connection
# importar datatime para crear el delta de tiempo
from datetime import datetime, timedelta


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # ------------------------tabla de vuelos------------------------------------------
    # 1. funcion obtener vuelos--------------------------------------------------------------
    # filtros
    def buscar_tabla_vuelos(self, fecha):
        """
        It does nothing.
        """

        # Convertir la fecha de entrada a datetime para obtener el siguiente día
        # Convertir la fecha de entrada a un objeto datetime
        fecha_seleccionada = datetime.strptime( fecha, "%Y-%m-%d %H:%M:%S")  
        # Buscar el vuelo la fecha 5 días después de la fecha seleccionada
        fecha_siguiente = fecha_seleccionada + timedelta( days=5)  
        # Convertir la fecha siguiente a una cadena en formato 'YYYY-MM-DD'
        fecha_siguiente_str = fecha_siguiente.strftime( "%Y-%m-%d")  

        # Crear la consulta SQL para seleccionar los vuelos entre la fecha seleccionada y la fecha siguiente
        query = f""" SELECT vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida
                FROM public.tabla_vuelos
                WHERE hora_salida >= '{fecha}' AND hora_salida < '{fecha_siguiente_str}'; """

        # El cursor y la conexión solo funcionan dentro del contexto del 'with'
        with self._open_connection() as conn:  # Abrir una conexión a la base de datos
            with conn.cursor() as cursor:  # Crear un cursor para ejecutar la consulta
                cursor.execute(query)  # Ejecutar la consulta SQL

                response = (
                    cursor.fetchall()
                )  # Obtener todos los resultados de la consulta

                # Obtener los nombres de las columnas de los resultados
                columnas = [columna.name for columna in cursor.description or []]

                # Crear una lista de diccionarios donde cada diccionario representa una fila de la tabla
                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                return objeto_contenidos  # Retornar la lista de diccionarios
