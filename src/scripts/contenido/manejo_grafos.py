import networkx as nx
import heapq
from datetime import datetime, timedelta


def construir_grafo_desde_vuelos(results):
    """
    Construye y devuelve el grafo utilizando los vuelos proporcionados.


    Args:
    - results: Resultados de la consulta SQL con estructura (vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida)


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
        hora_llegada = hora_salida + timedelta(hours=duracion)


        # Agregar nodos si no existen
        grafo.add_node(origen)
        grafo.add_node(destino)


        # Agregar arista (vuelo directo)
        grafo.add_edge(origen, destino, price=precio, duration=duracion, 
                       departure_time=hora_salida, arrival_time=hora_llegada)


    return grafo


def encontrar_ruta_optima_dijkstra(results, origen, destino, orden, max_escalas):
    """
    Encuentra la ruta óptima desde origen hasta destino en el grafo construido a partir de los resultados,
    según el criterio especificado y considerando un número máximo de escalas.


    Args:
    - results: Resultados de la consulta SQL con estructura (vuelo_origen, vuelo_destino, precio_vuelo, duracion_vuelo, hora_salida)
    - origen: Ciudad de origen.
    - destino: Ciudad de destino.
    - orden: Criterio de orden ('precio' o 'tiempo').
    - max_escalas: Número máximo de escalas permitidas.


    Returns:
    - Ruta óptima como lista de diccionarios con detalles del vuelo.
    """
    grafo_vuelos = construir_grafo_desde_vuelos(results)
    print(grafo_vuelos.edges)


    # Crear una cola de prioridad para Dijkstra
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, origen, 0, [origen], [], 0.0))  # (costo, nodo_actual, escalas, camino, detalles_vuelos, tiempo_total)


    mejor_costo = {origen: 0}
    mejor_escalas = {origen: 0}


    while cola_prioridad:
        costo_actual, nodo_actual, escalas_actual, camino, detalles_vuelos, tiempo_total = heapq.heappop(cola_prioridad)


        if nodo_actual == destino:
            if escalas_actual <= max_escalas:
                return detalles_vuelos, costo_actual, tiempo_total


        if escalas_actual > max_escalas:
            continue


        for vecino in grafo_vuelos.neighbors(nodo_actual):
            arista = grafo_vuelos[nodo_actual][vecino]
            costo_nuevo = costo_actual + (arista['price'] if orden == 'precio' else arista['duration'])
            escalas_nuevas = escalas_actual + 1


            # Si se busca optimizar por tiempo, agregar el tiempo de espera entre vuelos
            tiempo_total_nuevo = tiempo_total + arista['duration']
            if orden == 'tiempo':
                if detalles_vuelos:
                    ultimo_vuelo = detalles_vuelos[-1]
                    tiempo_espera = (arista['departure_time'] - datetime.strptime(ultimo_vuelo['hora_llegada'], '%Y-%m-%d %H:%M:%S')).total_seconds() / 3600.0  # Convertir a horas
                    if tiempo_espera < 0:  # Si el vuelo sale antes del anterior (no debería ocurrir)
                        continue  # Ignorar este vuelo de conexión
                    tiempo_total_nuevo += tiempo_espera


            if vecino not in mejor_costo or costo_nuevo < mejor_costo[vecino] or escalas_nuevas < mejor_escalas[vecino]:
                mejor_costo[vecino] = costo_nuevo
                mejor_escalas[vecino] = escalas_nuevas
                detalles_vuelos_nuevos = detalles_vuelos + [{
                    'origen': nodo_actual,
                    'destino': vecino,
                    'precio': arista['price'],
                    'duracion': arista['duration'],
                    'hora_salida': arista['departure_time'].strftime('%Y-%m-%d %H:%M:%S'),
                    'hora_llegada': arista['arrival_time'].strftime('%Y-%m-%d %H:%M:%S')
                }]
                heapq.heappush(cola_prioridad, (costo_nuevo, vecino, escalas_nuevas, camino + [vecino], detalles_vuelos_nuevos, tiempo_total_nuevo))


    return None, None, None


# Ejemplo de uso para testeo
# if __name__ == "__main__":
#     results = [
#         {"vuelo_origen": "A", "vuelo_destino": "B", "precio_vuelo": 20, "duracion_vuelo": 1, "hora_salida": "2024-07-01 08:00:00"},
#         {"vuelo_origen": "B", "vuelo_destino": "C", "precio_vuelo": 10, "duracion_vuelo": 1, "hora_salida": "2024-07-01 09:00:00"},
#         {"vuelo_origen": "C", "vuelo_destino": "D", "precio_vuelo": 30, "duracion_vuelo": 1, "hora_salida": "2024-07-01 10:00:00"},
#         {"vuelo_origen": "D", "vuelo_destino": "E", "precio_vuelo": 10, "duracion_vuelo": 1, "hora_salida": "2024-07-01 11:00:00"},
#         {"vuelo_origen": "C", "vuelo_destino": "E", "precio_vuelo": 50, "duracion_vuelo": 1, "hora_salida": "2024-07-01 12:00:00"},
#     ]


#     ruta, costo_total, tiempo_total = encontrar_ruta_optima_dijkstra(results, "A", "E", "precio", 3)
#     print("Ruta óptima por precio:", ruta)
#     print("Costo total por precio:", costo_total)


#     ruta, costo_total, tiempo_total = encontrar_ruta_optima_dijkstra(results, "A", "E", "tiempo", 3)
#     print("Ruta óptima por tiempo:", ruta)
#     print("Costo total por tiempo (horas):", tiempo_total)




