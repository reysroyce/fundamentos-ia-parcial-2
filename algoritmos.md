# ALGORITMOS PARA EL RECONOCIMIENTO DE DÍGITOS

## 1. BFS (Búsqueda en anchura)
Recorre los nodos por niveles, comenzando desde el nodo inicial. Permite revisar diferentes posibilidades.

## 2. DFS (Búsqueda en profundidad)
Explora una ruta hasta llegar al final y después regresa para revisar otras opciones.

## 3. A* (Búsqueda heurística)

Utiliza la fórmula:

f(n) = g(n) + h(n)

- g(n): costo del recorrido.
- h(n): estimación del costo restante.

Ayuda a encontrar el dígito más parecido.

## 4. Algoritmo genético

Utiliza una población de soluciones para mejorar el reconocimiento.

- Cromosoma: conjunto de pesos.
- Fitness: precisión de clasificación.
- Cruce: combinación de soluciones.
- Mutación: cambio aleatorio de valores.
- Parada: alcanzar una precisión o número de generaciones.

## 5. Flujo completo

1. Recibir imagen.
2. Extraer características.
3. Analizar líneas, curvas y huecos.
4. Construir el grafo.
5. Aplicar algoritmos de búsqueda.
6. Identificar el dígito.
7. Mostrar el resultado.

## Conclusión
Estos algoritmos permiten explorar diferentes opciones y mejorar el reconocimiento de imágenes mediante características como líneas, curvas, huecos y simetría.
