import networkx as nx


def construir_grafo_desde_vuelos(results):
    """
    Construye y devuelve el grafo utilizando los vuelos proporcionados.

    Args:
    - results: Resultados de la consulta SQL con estructura (vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida)

    Returns:
    - grafo: Grafo construido a partir de los vuelos.
    """
    # grafo
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

        # Agregar arista (vuelo directo)
        grafo.add_edge(
            origen, destino, price=precio, duration=duracion, departure_time=hora_salida
        )

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
    grafo_vuelos = construir_grafo_desde_vuelos(results)

    
    try:
        if orden == "precio":
            ruta_optima = nx.shortest_path(
                grafo_vuelos, source=origen, target=destino, weight="price"
            )
        elif orden == "tiempo":
            ruta_optima = nx.shortest_path(
                grafo_vuelos, source=origen, target=destino, weight="duration"
            )
            print(ruta_optima)
        else:
            raise ValueError("Orden no válido. Debe ser 'precio' o 'tiempo'.")

        return ruta_optima

    except nx.NetworkXNoPath:
        return None
