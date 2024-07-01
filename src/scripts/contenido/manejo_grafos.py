import networkx as nx
from datetime import datetime, timedelta


def construir_grafo_desde_vuelos(results, include_wait_time=False):
    """
    Construye y devuelve el grafo utilizando los vuelos proporcionados.


    Args:
    - results: Resultados de la consulta SQL con estructura (vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida)
    - include_wait_time: Booleano que indica si se debe incluir el tiempo de espera entre vuelos como parte del peso de la arista.


    Returns:
    - grafo: Grafo construido a partir de los vuelos.
    """
    grafo = nx.DiGraph()





    for vuelo in results:
        origen = vuelo["vuelo_origen"]
        destino = vuelo["vuelo_destino"]
        precio = vuelo["precio_vuelo"]
        duracion = vuelo["duracion_vuelo"]
        hora_salida = vuelo["hora_salida"]


        # Agregar nodos si no existen
        grafo.add_node(origen)
        grafo.add_node(destino)

        

        # Calcular tiempo de espera (en horas) entre vuelos si se solicita
        if include_wait_time:
            hora_salida_siguiente = hora_salida+ timedelta(hours=duracion)
            tiempo_espera = (hora_salida_siguiente - hora_salida).total_seconds() / 3600
        else:
            tiempo_espera = 0


        # Calcular peso de la arista
        if include_wait_time:
            peso_arista = duracion + tiempo_espera
        else:
            peso_arista = duracion


        # Agregar arista (vuelo directo)
        grafo.add_edge(origen, destino, price=precio, duration=duracion, departure_time=hora_salida, weight=peso_arista)


    return grafo


def encontrar_ruta_optima(results, origen, destino, orden):
    """
    Encuentra la ruta óptima desde origen hasta destino en el grafo construido a partir de los resultados,
    según el criterio especificado.


    Args:
    - results: Resultados de la consulta SQL con estructura (vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida)
    - origen: Ciudad de origen.
    - destino: Ciudad de destino.
    - orden: Criterio de orden ('precio' o 'tiempo').


    Returns:
    - Lista de ciudades representando la ruta óptima.
    """
    try:
        if orden == "precio":
            grafo_vuelos = construir_grafo_desde_vuelos(results)
            ruta_optima = nx.shortest_path(grafo_vuelos, source=origen, target=destino, weight="price")
        elif orden == "tiempo":
            grafo_vuelos = construir_grafo_desde_vuelos(results, include_wait_time=True)
            ruta_optima = nx.shortest_path(grafo_vuelos, source=origen, target=destino, weight="weight")
        else:
            raise ValueError("Orden no válido. Debe ser 'precio' o 'tiempo'.")


        return ruta_optima


    except nx.NetworkXNoPath:
        return None






