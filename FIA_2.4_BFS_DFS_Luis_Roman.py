"""
Actividad 2.4: Búsqueda Ciega (BFS y DFS)
=========================================
Implementación completa de Búsqueda en Anchura (BFS) y Búsqueda en Profundidad (DFS)
aplicada a dos problemas clásicos:
 1. Resolución de Laberintos (Grid 2D)
 2. Juego del 8-Puzzle

Incluye métricas de rendimiento (tiempo, nodos visitados, longitud de ruta)
y un menú interactivo en consola.
"""

import time
import os
from collections import deque


# ==============================================================================
# PARTE 1: LABERINTO 2D (BFS vs DFS)
# ==============================================================================

LABERINTO_EJEMPLO = [
    ['S', 0, 1, 0, 0, 0],
    [0,   0, 1, 0, 1, 0],
    [0,   1, 0, 0, 1, 0],
    [0,   0, 0, 1, 0, 0],
    [1,   1, 0, 0, 0, 'G']
]

def renderizar_laberinto(lab, camino=None):
    """Imprime el laberinto en formato ASCII visual."""
    camino_set = set(camino) if camino else set()
    columnas = len(lab[0])
    
    print("  +" + "---+" * columnas)
    for r in range(len(lab)):
        fila_str = f"{r} |"
        for c in range(columnas):
            val = lab[r][c]
            if (r, c) in camino_set and val not in ('S', 'G'):
                fila_str += " * |"
            elif val == 1:
                fila_str += " █ |"
            elif val == 0:
                fila_str += "   |"
            else:
                fila_str += f" {val} |"
        print(fila_str)
        print("  +" + "---+" * columnas)

def obtener_vecinos_laberinto(pos, lab):
    """Retorna posiciones adyacentes válidas (Arriba, Abajo, Izquierda, Derecha)."""
    r, c = pos
    filas, cols = len(lab), len(lab[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vecinos = []

    for dr, dc in movimientos:
        nr, nc = r + dr, c + dc
        if 0 <= nr < filas and 0 <= nc < cols and lab[nr][nc] != 1:
            vecinos.append((nr, nc))
    return vecinos

def bfs_laberinto(lab, inicio, meta):
    """Algoritmo de Búsqueda en Anchura (BFS) para laberintos."""
    cola = deque([(inicio, [inicio])])
    visitados = {inicio}
    nodos_explorados = 0

    while cola:
        actual, camino = cola.popleft()
        nodos_explorados += 1

        if actual == meta:
            return camino, nodos_explorados

        for vecino in obtener_vecinos_laberinto(actual, lab):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))

    return None, nodos_explorados

def dfs_laberinto(lab, inicio, meta):
    """Algoritmo de Búsqueda en Profundidad (DFS) para laberintos."""
    pila = [(inicio, [inicio])]
    visitados = {inicio}
    nodos_explorados = 0

    while pila:
        actual, camino = pila.pop()
        nodos_explorados += 1

        if actual == meta:
            return camino, nodos_explorados

        for vecino in obtener_vecinos_laberinto(actual, lab):
            if vecino not in visitados:
                visitados.add(vecino)
                pila.append((vecino, camino + [vecino]))

    return None, nodos_explorados

def ejecutar_seccion_laberinto():
    """Ejecuta y compara BFS y DFS en el problema del laberinto."""
    inicio = (0, 0)
    meta = (4, 5)

    print("\n" + "=" * 60)
    print("           LABERINTO: CONFIGURACIÓN INICIAL")
    print("=" * 60)
    renderizar_laberinto(LABERINTO_EJEMPLO)

    # Medición BFS
    t0 = time.perf_counter()
    camino_bfs, nodos_bfs = bfs_laberinto(LABERINTO_EJEMPLO, inicio, meta)
    t_bfs = (time.perf_counter() - t0) * 1000

    # Medición DFS
    t0 = time.perf_counter()
    camino_dfs, nodos_dfs = dfs_laberinto(LABERINTO_EJEMPLO, inicio, meta)
    t_dfs = (time.perf_counter() - t0) * 1000

    print("\n>>> SOLUCIÓN BFS (Garantiza Ruta Óptima) <<<")
    renderizar_laberinto(LABERINTO_EJEMPLO, camino_bfs)

    print("\n>>> SOLUCIÓN DFS <<<")
    renderizar_laberinto(LABERINTO_EJEMPLO, camino_dfs)

    print("\n" + "=" * 60)
    print("               CUADRO COMPARATIVO - LABERINTO")
    print("=" * 60)
    print(f"{'Métrica':<25} | {'BFS':<15} | {'DFS':<15}")
    print("-" * 60)
    print(f"{'Longitud de Ruta (pasos)':<25} | {len(camino_bfs)-1 if camino_bfs else 'N/A':<15} | {len(camino_dfs)-1 if camino_dfs else 'N/A':<15}")
    print(f"{'Nodos Explorados':<25} | {nodos_bfs:<15} | {nodos_dfs:<15}")
    print(f"{'Tiempo de Ejecución (ms)':<25} | {t_bfs:<15.4f} | {t_dfs:<15.4f}")
    print("=" * 60)


# ==============================================================================
# PARTE 2: 8-PUZZLE (BFS vs DFS)
# ==============================================================================

ESTADO_META_PUZZLE = (1, 2, 3, 
                      4, 5, 6, 
                      7, 8, 0)

ESTADO_INICIAL_PUZZLE = (1, 2, 3, 
                         4, 0, 6, 
                         7, 5, 8)

def renderizar_puzzle(estado):
    """Muestra el tablero de 3x3 del 8-puzzle."""
    print("  +---+---+---+")
    for i in range(0, 9, 3):
        fila = [str(x) if x != 0 else " " for x in estado[i:i+3]]
        print(f"  | {' | '.join(fila)} |")
        print("  +---+---+---+")

def obtener_sucesores_puzzle(estado):
    """Genera configuraciones alcanzables deslizando el espacio vacío (0)."""
    sucesores = []
    idx = estado.index(0)
    r, c = divmod(idx, 3)

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in movimientos:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nuevo_idx = nr * 3 + nc
            nuevo_estado = list(estado)
            nuevo_estado[idx], nuevo_estado[nuevo_idx] = nuevo_estado[nuevo_idx], nuevo_estado[idx]
            sucesores.append(tuple(nuevo_estado))

    return sucesores

def bfs_puzzle(inicio, meta):
    """BFS para resolver el 8-puzzle."""
    cola = deque([(inicio, [inicio])])
    visitados = {inicio}
    nodos_explorados = 0

    while cola:
        actual, camino = cola.popleft()
        nodos_explorados += 1

        if actual == meta:
            return camino, nodos_explorados

        for sig in obtener_sucesores_puzzle(actual):
            if sig not in visitados:
                visitados.add(sig)
                cola.append((sig, camino + [sig]))

    return None, nodos_explorados

def dfs_puzzle(inicio, meta, limite_profundidad=20):
    """DFS con límite de profundidad para evitar loops infinitos en 8-puzzle."""
    pila = [(inicio, [inicio])]
    visitados = {inicio}
    nodos_explorados = 0

    while pila:
        actual, camino = pila.pop()
        nodos_explorados += 1

        if actual == meta:
            return camino, nodos_explorados

        if len(camino) <= limite_profundidad:
            for sig in obtener_sucesores_puzzle(actual):
                if sig not in visitados:
                    visitados.add(sig)
                    pila.append((sig, camino + [sig]))

    return None, nodos_explorados

def ejecutar_seccion_puzzle():
    """Ejecuta y compara BFS y DFS en el 8-puzzle."""
    print("\n" + "=" * 60)
    print("             8-PUZZLE: CONFIGURACIÓN")
    print("=" * 60)
    print("Estado Inicial:")
    renderizar_puzzle(ESTADO_INICIAL_PUZZLE)
    print("\nEstado Meta:")
    renderizar_puzzle(ESTADO_META_PUZZLE)

    print("\n[+] Calculando solución con BFS...")
    t0 = time.perf_counter()
    camino_bfs, nodos_bfs = bfs_puzzle(ESTADO_INICIAL_PUZZLE, ESTADO_META_PUZZLE)
    t_bfs = (time.perf_counter() - t0) * 1000

    print("[+] Calculando solución con DFS (profundidad máx: 20)...")
    t0 = time.perf_counter()
    camino_dfs, nodos_dfs = dfs_puzzle(ESTADO_INICIAL_PUZZLE, ESTADO_META_PUZZLE, limite_profundidad=20)
    t_dfs = (time.perf_counter() - t0) * 1000

    print("\n" + "=" * 60)
    print("               CUADRO COMPARATIVO - 8-PUZZLE")
    print("=" * 60)
    print(f"{'Métrica':<25} | {'BFS':<15} | {'DFS (Límite 20)':<15}")
    print("-" * 60)
    print(f"{'Pasos de la Solución':<25} | {len(camino_bfs)-1 if camino_bfs else 'N/A':<15} | {len(camino_dfs)-1 if camino_dfs else 'Sin solución':<15}")
    print(f"{'Nodos Evaluados':<25} | {nodos_bfs:<15} | {nodos_dfs:<15}")
    print(f"{'Tiempo de Ejecución (ms)':<25} | {t_bfs:<15.4f} | {t_dfs:<15.4f}")
    print("=" * 60)

    if camino_bfs:
        opc = input("\n¿Deseas animar la secuencia paso a paso solución BFS? (s/n): ")
        if opc.lower() == 's':
            for paso, estado in enumerate(camino_bfs):
                print(f"\n--- Paso {paso} ---")
                renderizar_puzzle(estado)
                time.sleep(0.4)


# ==============================================================================
# MENÚ PRINCIPAL INTERACTIVO
# ==============================================================================

def main():
    while True:
        print("\n" + "=" * 60)
        print("    ACTIVIDAD 2.4: BÚSQUEDA CIEGA EN IA (BFS vs DFS)")
        print("=" * 60)
        print(" 1. Demostración Laberinto 2D (BFS vs DFS)")
        print(" 2. Demostración 8-Puzzle (BFS vs DFS)")
        print(" 3. Ejecutar Ambas Pruebas Completa")
        print(" 4. Salir")
        print("=" * 60)
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            ejecutar_seccion_laberinto()
        elif opcion == '2':
            ejecutar_seccion_puzzle()
        elif opcion == '3':
            ejecutar_seccion_laberinto()
            ejecutar_seccion_puzzle()
        elif opcion == '4':
            print("\n¡Ejecución finalizada con éxito!")
            break
        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    main()