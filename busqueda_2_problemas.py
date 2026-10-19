"""
Fundamentos de Inteligencia Artificial — Actividad 2.1
Modelado de dos problemas como búsqueda:
A) Ruta de reparto con costos ponderados (Dijkstra).
B) Laberinto con movimientos de costo uniforme (BFS).

Autor: Luis Antonio Roman Rey
Requisitos: Python 3.10+; no requiere paquetes externos.
"""

from heapq import heappush, heappop
from collections import deque


def dijkstra(graph, start, goal):
    """Devuelve (ruta, costo, expandidos) para un grafo con pesos no negativos."""
    distances = {node: float("inf") for node in graph}
    previous = {}
    distances[start] = 0
    queue = [(0, start)]
    expanded = 0

    while queue:
        cost, node = heappop(queue)
        # Ignorar entradas antiguas de la cola de prioridad.
        if cost != distances[node]:
            continue
        expanded += 1
        if node == goal:
            break

        for neighbor, edge_cost in graph[node].items():
            if edge_cost < 0:
                raise ValueError("Dijkstra requiere pesos no negativos.")
            new_cost = cost + edge_cost
            if new_cost < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_cost
                previous[neighbor] = node
                heappush(queue, (new_cost, neighbor))

    if distances.get(goal, float("inf")) == float("inf"):
        return [], float("inf"), expanded

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = previous[node]
    path.append(start)
    path.reverse()
    return path, distances[goal], expanded


def bfs_maze(grid, start, goal):
    """BFS sobre una cuadrícula; # es pared, . es celda transitable."""
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    previous = {start: None}
    expanded = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        current = queue.popleft()
        expanded += 1
        if current == goal:
            break

        for dr, dc in moves:
            nxt = (current[0] + dr, current[1] + dc)
            r, c = nxt
            inside = 0 <= r < rows and 0 <= c < cols
            if not inside or grid[r][c] == "#":
                continue
            if nxt not in previous:
                previous[nxt] = current
                queue.append(nxt)

    if goal not in previous:
        return [], expanded

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path, expanded


def print_maze_solution(grid, path):
    """Imprime el laberinto marcando la ruta con * y los extremos con S/G."""
    visual = [list(row) for row in grid]
    for r, c in path:
        if visual[r][c] == ".":
            visual[r][c] = "*"
    if path:
        sr, sc = path[0]
        gr, gc = path[-1]
        visual[sr][sc] = "S"
        visual[gr][gc] = "G"
    print("\n".join("".join(row) for row in visual))


def main():
    # PROBLEMA A: ubicaciones y distancias estimadas (km), grafo no dirigido.
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2},
        "E": {"C": 10, "D": 2},
    }
    path, cost, expanded = dijkstra(graph, "A", "D")
    print("=== PROBLEMA A: RUTA DE REPARTO ===")
    print("Inicio: A | Meta: D")
    print("Ruta óptima:", " -> ".join(path) if path else "No existe ruta")
    print(f"Costo total: {cost} km" if path else "Costo total: infinito")
    print("Nodos expandidos:", expanded)

    # PROBLEMA B: laberinto. Cada movimiento válido cuesta 1.
    grid = [
        "......",
        ".##.#.",
        "...#..",
        "#.....",
        "......",
    ]
    start, goal = (0, 0), (4, 5)
    maze_path, maze_expanded = bfs_maze(grid, start, goal)
    print("\n=== PROBLEMA B: LABERINTO ===")
    print("Inicio:", start, "| Meta:", goal)
    if maze_path:
        print("Ruta (fila, columna):", " -> ".join(map(str, maze_path)))
        print("Número de movimientos:", len(maze_path) - 1)
    else:
        print("No existe una ruta entre el inicio y la meta.")
    print("Estados expandidos:", maze_expanded)
    print("Laberinto (* = ruta):")
    print_maze_solution(grid, maze_path)


if __name__ == "__main__":
    main()
