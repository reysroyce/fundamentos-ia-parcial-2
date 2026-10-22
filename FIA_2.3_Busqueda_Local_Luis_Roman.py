"""
Actividad 2.3 — Búsqueda local: Hill Climbing y Simulated Annealing
Autor: Luis Antonio Roman Rey
Caso ilustrativo: ruta de reparto por ocho ubicaciones con coordenadas sintéticas.

Requisitos: Python 3.10+ y matplotlib.
Ejecución: python FIA_2.3_Busqueda_Local_Luis_Roman.py
Genera la gráfica FIA_2.3_grafica_convergencia.png.
"""
from math import hypot, exp
import random
import matplotlib.pyplot as plt

# Datos sintéticos en un plano; las distancias son kilómetros ilustrativos.
LOCATIONS = {
    "Centro": (0, 0), "Norte": (2, 6), "Mercado": (3, 2),
    "Hospital": (6, 5), "Escuela": (7, 1), "Parque": (1, 4),
    "Bodega": (5, 7), "Sur": (4, -2)
}
NAMES = list(LOCATIONS)
START = "Centro"
SEED = 42

def distance(a, b):
    """Calcula la distancia euclidiana entre dos ubicaciones."""
    ax, ay = LOCATIONS[a]
    bx, by = LOCATIONS[b]
    return hypot(ax - bx, ay - by)

def route_cost(route):
    """Suma el costo de cada tramo, incluido el regreso al origen."""
    return sum(distance(route[i], route[(i + 1) % len(route)])
               for i in range(len(route)))

def random_route(rng):
    """Genera una ruta aleatoria manteniendo Centro como punto inicial."""
    rest = [name for name in NAMES if name != START]
    rng.shuffle(rest)
    return [START] + rest

def neighbor(route, rng):
    """Genera un vecino intercambiando dos paradas, sin mover el origen."""
    candidate = route[:]
    i, j = rng.sample(range(1, len(candidate)), 2)
    candidate[i], candidate[j] = candidate[j], candidate[i]
    return candidate

def hill_climbing(iterations=500, seed=SEED):
    """Acepta solamente vecinos cuyo costo sea menor."""
    rng = random.Random(seed)
    current = random_route(rng)
    current_cost = route_cost(current)
    best, best_cost = current[:], current_cost
    history = []
    for _ in range(iterations):
        candidate = neighbor(current, rng)
        candidate_cost = route_cost(candidate)
        if candidate_cost < current_cost:
            current, current_cost = candidate, candidate_cost
        if current_cost < best_cost:
            best, best_cost = current[:], current_cost
        history.append(best_cost)
    return best, best_cost, history

def simulated_annealing(iterations=500, initial_temperature=20.0,
                        cooling_rate=0.995, seed=SEED):
    """Puede aceptar empeoramientos con probabilidad exp(-delta/T)."""
    rng = random.Random(seed)
    current = random_route(rng)
    current_cost = route_cost(current)
    best, best_cost = current[:], current_cost
    temperature = initial_temperature
    history = []
    for _ in range(iterations):
        candidate = neighbor(current, rng)
        candidate_cost = route_cost(candidate)
        delta = candidate_cost - current_cost
        if delta < 0 or rng.random() < exp(-delta / max(temperature, 1e-12)):
            current, current_cost = candidate, candidate_cost
        if current_cost < best_cost:
            best, best_cost = current[:], current_cost
        history.append(best_cost)
        temperature *= cooling_rate
    return best, best_cost, history

def show_result(name, route, cost):
    print("\n" + name)
    print("Ruta: " + " -> ".join(route + [route[0]]))
    print(f"Distancia total ilustrativa: {cost:.2f} km")

def main():
    iterations = 500
    hc_route, hc_cost, hc_history = hill_climbing(iterations, SEED)
    sa_route, sa_cost, sa_history = simulated_annealing(
        iterations, initial_temperature=20.0, cooling_rate=0.995, seed=SEED
    )
    print("FIA 2.3 — Comparación de algoritmos de búsqueda local")
    print(f"Ubicaciones: {len(LOCATIONS)} | Iteraciones por algoritmo: {iterations}")
    show_result("Hill Climbing", hc_route, hc_cost)
    show_result("Simulated Annealing", sa_route, sa_cost)
    print("\nNota: se usan coordenadas sintéticas y una semilla fija para reproducibilidad.")

    plt.figure(figsize=(9, 5.2))
    plt.plot(range(1, iterations + 1), hc_history, label="Hill Climbing")
    plt.plot(range(1, iterations + 1), sa_history, label="Simulated Annealing")
    plt.xlabel("Iteración")
    plt.ylabel("Mejor distancia encontrada (km ilustrativos)")
    plt.title("Convergencia de los algoritmos de búsqueda local")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("FIA_2.3_grafica_convergencia.png", dpi=180)
    print("Gráfica guardada como FIA_2.3_grafica_convergencia.png")

if __name__ == "__main__":
    main()
