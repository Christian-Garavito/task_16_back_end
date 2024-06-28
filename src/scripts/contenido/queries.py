""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # ------------------------tabla_contenido_imdb------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_contenidos(self, filtros):
        """
        It does nothing.
        """
        pagina = 1
        limit = 5

        query = """SELECT 
                        tc.pk_id_peliculas
                        ,tc.titulo_pelicula
                        ,tc.ano_pelicula
                        ,tc.director_pelicula
                        ,tc.valor_pelicula
                        ,tc.fk_id_tipo_contenido 
                        ,ttc.tipo_contenido
                    FROM tabla_contenido_imdb tc
                    INNER JOIN tipo_contenido ttc
                    ON tc.fk_id_tipo_contenido = ttc.pk_id_tipo_contenido"""
        # print("--------------------------------------------------------")
        if filtros:
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

        pagina = int(limit) * (int(pagina) - 1)

        # ordenar la tabla
        query += f" ORDER BY pk_id_peliculas OFFSET {pagina} "
        
        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchmany(int(limit))

                columnas = [columna.name for columna in cursor.description or []]

                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                return objeto_contenidos, bool(cursor.fetchone())

