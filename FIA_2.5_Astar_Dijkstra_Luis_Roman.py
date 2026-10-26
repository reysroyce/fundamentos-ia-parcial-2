"""
Actividad 2.5: Búsqueda Informada (Dijkstra y A*)
=================================================
Implementación completa de los algoritmos Dijkstra y A* (A-Star)
para resolver problemas de búsqueda en grafos con pesos y cuadrículas 2D.

Incluye:
 - Uso de Colas de Prioridad (`heapq`)
 - Heurísticas (Distancia Manhattan y Euclidiana)
 - Análisis de Eficiencia, Costos y Nodos Explorados
 - Cuadro Comparativo Integrado
"""

import heapq
import math
import time


# ==============================================================================
# PARTE 1: BÚSQUEDA EN GRAFO CON PESOS
# ==============================================================================

# Grafo ponderado de ciudades/nodos
GRAFO_EJEMPLO = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
    'E': [('C', 10), ('D', 2), ('Z', 3)],
    'Z': [('D', 6), ('E', 3)]
}

# Coordenadas geográficas aproximadas para cálculo heurístico (h(n))
COORDENADAS_GRAFO = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (1, 1),
    'D': (5, 4),
    'E': (4, 1),
    'Z': (7, 2)
}

def heuristica_grafo(nodo, destino):
    """Calcula la distancia euclidiana entre coordenadas de dos nodos."""
    x1, y1 = COORDENADAS_GRAFO[nodo]
    x2, y2 = COORDENADAS_GRAFO[destino]
    return math.hypot(x2 - x1, y2 - y1)

def dijkstra_grafo(grafo, inicio, destino):
    """Algoritmo de Dijkstra para encontrar la ruta de costo mínimo."""
    pila_prioridad = [(0, inicio, [inicio])] # (costo_acumulado, nodo_actual, ruta)
    visitados = {}
    nodos_explorados = 0

    while pila_prioridad:
        costo_actual, actual, ruta = heapq.heappop(pila_prioridad)
        nodos_explorados += 1

        if actual == destino:
            return ruta, costo_actual, nodos_explorados

        if actual in visitados and visitados[actual] <= costo_actual:
            continue
        visitados[actual] = costo_actual

        for vecino, peso in grafo.get(actual, []):
            nuevo_costo = costo_actual + peso
            if vecino not in visitados or nuevo_costo < visitados[vecino]:
                heapq.heappush(pila_prioridad, (nuevo_costo, vecino, ruta + [vecino]))

    return None, float('inf'), nodos_explorados

def a_estrella_grafo(grafo, inicio, destino):
    """Algoritmo A* utilizando costo g(n) y heurística h(n)."""
    pila_prioridad = [(0 + heuristica_grafo(inicio, destino), 0, inicio, [inicio])]
    visitados = {}
    nodos_explorados = 0

    while pila_prioridad:
        f_val, g_val, actual, ruta = heapq.heappop(pila_prioridad)
        nodos_explorados += 1

        if actual == destino:
            return ruta, g_val, nodos_explorados

        if actual in visitados and visitados[actual] <= g_val:
            continue
        visitados[actual] = g_val

        for vecino, peso in grafo.get(actual, []):
            nuevo_g = g_val + peso
            if vecino not in visitados or nuevo_g < visitados[vecino]:
                f_nuevo = nuevo_g + heuristica_grafo(vecino, destino)
                heapq.heappush(pila_prioridad, (f_nuevo, nuevo_g, vecino, ruta + [vecino]))

    return None, float('inf'), nodos_explorados

def ejecutar_seccion_grafo():
    """Compara Dijkstra y A* en un grafo ponderado."""
    inicio, destino = 'A', 'Z'

    print("\n" + "=" * 60)
    print("          PRUEBA 1: BÚSQUEDA EN GRAFO PONDERADO")
    print("=" * 60)

    # Dijkstra
    t0 = time.perf_counter()
    ruta_d, costo_d, nodos_d = dijkstra_grafo(GRAFO_EJEMPLO, inicio, destino)
    t_d = (time.perf_counter() - t0) * 1000

    # A*
    t0 = time.perf_counter()
    ruta_a, costo_a, nodos_a = a_estrella_grafo(GRAFO_EJEMPLO, inicio, destino)
    t_a = (time.perf_counter() - t0) * 1000

    print(f"Origen: {inicio} | Destino: {destino}")
    print(f"\n- Dijkstra -> Ruta: {' -> '.join(ruta_d)} | Costo Total: {costo_d}")
    print(f"- A*       -> Ruta: {' -> '.join(ruta_a)} | Costo Total: {costo_a}")

    print("\n" + "=" * 60)
    print("             CUADRO COMPARATIVO - GRAFO")
    print("=" * 60)
    print(f"{'Métrica':<25} | {'Dijkstra':<15} | {'A* (A-Star)':<15}")
    print("-" * 60)
    print(f"{'Costo Total de Ruta':<25} | {costo_d:<15} | {costo_a:<15}")
    print(f"{'Nodos Explorados':<25} | {nodos_d:<15} | {nodos_a:<15}")
    print(f"{'Tiempo de Ejecución (ms)':<25} | {t_d:<15.4f} | {t_a:<15.4f}")
    print("=" * 60)


# ==============================================================================
# PARTE 2: BÚSQUEDA EN MAPA GRID 2D CON COSTOS DE TERRENO
# ==============================================================================

# 1 = Normal (Costo 1), 5 = Terreno Difícil (Costo 5), 999 = Pared/Infranqueable
GRID_TERRENO = [
    [1, 1, 1, 5, 5, 1],
    [1, 999, 1, 5, 1, 1],
    [1, 999, 1, 1, 1, 1],
    [1, 1, 5, 5, 999, 1],
    [1, 1, 1, 1, 1, 1]
]

def heuristica_manhattan(p1, p2):
    """Calcula la distancia Manhattan |x1 - x2| + |y1 - y2|."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def obtener_vecinos_grid(pos, grid):
    """Obtiene vecinos adyacentes y su costo de movimiento."""
    r, c = pos
    filas, cols = len(grid), len(grid[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vecinos = []

    for dr, dc in movimientos:
        nr, nc = r + dr, c + dc
        if 0 <= nr < filas and 0 <= nc < cols and grid[nr][nc] != 999:
            costo_terreno = grid[nr][nc]
            vecinos.append(((nr, nc), costo_terreno))

    return vecinos

def dijkstra_grid(grid, inicio, meta):
    """Dijkstra aplicado a un grid 2D con costos ponderados."""
    pq = [(0, inicio, [inicio])]
    visitados = {}
    nodos_explorados = 0

    while pq:
        costo_g, actual, camino = heapq.heappop(pq)
        nodos_explorados += 1

        if actual == meta:
            return camino, costo_g, nodos_explorados

        if actual in visitados and visitados[actual] <= costo_g:
            continue
        visitados[actual] = costo_g

        for vecino, costo_mov in obtener_vecinos_grid(actual, grid):
            nuevo_costo = costo_g + costo_mov
            if vecino not in visitados or nuevo_costo < visitados[vecino]:
                heapq.heappush(pq, (nuevo_costo, vecino, camino + [vecino]))

    return None, float('inf'), nodos_explorados

def a_estrella_grid(grid, inicio, meta):
    """Algoritmo A* aplicado a un grid 2D usando distancia Manhattan."""
    pq = [(0 + heuristica_manhattan(inicio, meta), 0, inicio, [inicio])]
    visitados = {}
    nodos_explorados = 0

    while pq:
        f, g, actual, camino = heapq.heappop(pq)
        nodos_explorados += 1

        if actual == meta:
            return camino, g, nodos_explorados

        if actual in visitados and visitados[actual] <= g:
            continue
        visitados[actual] = g

        for vecino, costo_mov in obtener_vecinos_grid(actual, grid):
            nuevo_g = g + costo_mov
            if vecino not in visitados or nuevo_g < visitados[vecino]:
                f_nuevo = nuevo_g + heuristica_manhattan(vecino, meta)
                heapq.heappush(pq, (f_nuevo, nuevo_g, vecino, camino + [vecino]))

    return None, float('inf'), nodos_explorados

def renderizar_grid_solucion(grid, camino=None):
    """Muestra el grid con costos y la ruta óptima trazada."""
    camino_set = set(camino) if camino else set()
    print("  +" + "---+" * len(grid[0]))
    for r in range(len(grid)):
        fila_str = "|"
        for c in range(len(grid[0])):
            val = grid[r][c]
            if (r, c) in camino_set:
                fila_str += " * |"
            elif val == 999:
                fila_str += " █ |"
            else:
                fila_str += f" {val} |"
        print(fila_str)
        print("  +" + "---+" * len(grid[0]))

def ejecutar_seccion_grid():
    """Compara Dijkstra y A* en un mapa de terreno con pesos diferidos."""
    inicio = (0, 0)
    meta = (4, 5)

    print("\n" + "=" * 60)
    print("         PRUEBA 2: MAPA GRID 2D CON COSTOS DE TERRENO")
    print("=" * 60)
    print("Grid (1 = Normal, 5 = Dificil, █ = Pared):")
    renderizar_grid_solucion(GRID_TERRENO)

    # Dijkstra
    t0 = time.perf_counter()
    camino_d, costo_d, nodos_d = dijkstra_grid(GRID_TERRENO, inicio, meta)
    t_d = (time.perf_counter() - t0) * 1000

    # A*
    t0 = time.perf_counter()
    camino_a, costo_a, nodos_a = a_estrella_grid(GRID_TERRENO, inicio, meta)
    t_a = (time.perf_counter() - t0) * 1000

    print("\n>>> RUTA SELECCIONADA POR A* / DIJKSTRA <<<")
    renderizar_grid_solucion(GRID_TERRENO, camino_a)

    print("\n" + "=" * 60)
    print("             CUADRO COMPARATIVO - GRID 2D")
    print("=" * 60)
    print(f"{'Métrica':<25} | {'Dijkstra':<15} | {'A* (Manhattan)':<15}")
    print("-" * 60)
    print(f"{'Costo Total de Camino':<25} | {costo_d:<15} | {costo_a:<15}")
    print(f"{'Longitud de Pasos':<25} | {len(camino_d)-1 if camino_d else 'N/A':<15} | {len(camino_a)-1 if camino_a else 'N/A':<15}")
    print(f"{'Nodos Evaluados':<25} | {nodos_d:<15} | {nodos_a:<15}")
    print(f"{'Tiempo de Ejecución (ms)':<25} | {t_d:<15.4f} | {t_a:<15.4f}")
    print("=" * 60)


# ==============================================================================
# MENÚ PRINCIPAL INTERACTIVO
# ==============================================================================

def main():
    while True:
        print("\n" + "=" * 60)
        print("   ACTIVIDAD 2.5: BÚSQUEDA INFORMADA EN IA (DIJKSTRA vs A*)")
        print("=" * 60)
        print(" 1. Demostración en Grafo de Ciudades Ponderado")
        print(" 2. Demostración en Mapa Grid 2D con Costos")
        print(" 3. Ejecutar Ambas Demostraciones")
        print(" 4. Salir")
        print("=" * 60)

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == '1':
            ejecutar_seccion_grafo()
        elif opcion == '2':
            ejecutar_seccion_grid()
        elif opcion == '3':
            ejecutar_seccion_grafo()
            ejecutar_seccion_grid()
        elif opcion == '4':
            print("\n¡Ejecución finalizada con éxito!")
            break
        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    main()