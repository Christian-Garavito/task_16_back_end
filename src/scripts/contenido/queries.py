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
        pagina = 1
        limit = 20

        query = "SELECT x.* FROM public.tabla_vuelos x;"
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
        # query += " ORDER BY pk_id_peliculas"
        #query += f" ORDER BY pk_id_vuelo OFFSET {pagina} LIMIT {limit}"
        print(query)
        # pagina la trae como un string y para poderlo perar hay que
        # query += f" OFFSET {(paginas-1)*int(limit)} LIMIT {limit}"
        # print(query)

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                # print(response)
                # print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                # print(objeto_contenidos)

                return objeto_contenidos
