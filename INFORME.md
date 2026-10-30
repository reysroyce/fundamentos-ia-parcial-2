# Informe técnico: Reconocimiento de dígitos mediante búsqueda en grafos

## 1. Problema de búsqueda
El sistema recibe una imagen que representa un dígito y debe seleccionar una etiqueta del conjunto {0,1,2,3,4,5,6,7,8,9}. La imagen se normaliza a 28 × 28 píxeles y se representa mediante valores binarios. Los estados intermedios son la imagen normalizada, el vector de características y los candidatos. Las acciones consisten en extraer características, calcular distancias y expandir candidatos. La prueba objetivo consiste en seleccionar el candidato con menor coste. El coste es una distancia absoluta ponderada entre las características de la imagen y las del prototipo de cada dígito: C(x,d)=Σ wi|fi(x)-pi(d)|. La búsqueda resulta adecuada porque permite representar explícitamente los candidatos y comparar estrategias de exploración.

## 2. Grafo representativo
Se define G=(V,E), con V={Unknown,0,1,2,3,4,5,6,7,8,9}. Unknown representa la imagen sin clasificar y los diez nodos restantes son objetivos posibles. Se conectan Unknown con cada dígito. También se conectan candidatos cercanos para representar similitudes. El peso de una arista es una transformación normalizada de la distancia entre vectores: los costes pequeños representan mayor similitud y se muestran en una escala de 1 a 10. La visualización de la aplicación actualiza los pesos según la imagen procesada.

## 3. Algoritmos
**BFS:** utiliza una cola FIFO y visita los nodos por niveles. No utiliza los pesos, por lo que no garantiza el camino de coste mínimo en grafos ponderados.

**DFS:** utiliza una pila y explora una rama antes de retroceder. Puede encontrar una solución rápidamente, pero el resultado depende del orden de expansión y no es óptimo en general.

**A\*:** evalúa f(n)=g(n)+h(n), donde g(n) es el coste acumulado y h(n) estima el coste hasta el objetivo. Una heurística admisible no sobreestima el coste restante y permite obtener una solución óptima bajo las condiciones habituales de A*.

**Algoritmo genético:** el cromosoma es un vector de pesos de las características. El fitness representa la proporción de clasificaciones correctas en un conjunto de validación. Se aplican selección por torneo, cruce de un punto y mutación aleatoria. El proceso termina tras un número máximo de generaciones o al alcanzar el fitness objetivo.

## 4. Implementación y evaluación
El archivo `index.html` integra la carga o dibujo de una imagen, adaptación a 28×28, extracción de características por regiones, simetría, densidad y endpoints, cálculo de distancias, grafo y recorridos BFS/DFS/A*. Incluye un ajuste demostrativo de pesos mediante algoritmo genético y una prueba automática de 25 muestras sintéticas.

**Limitación importante:** los prototipos de esta entrega son patrones tipográficos creados en el navegador. Las pruebas sintéticas verifican el funcionamiento del código, pero no equivalen a una validación con MNIST ni demuestran generalización a escritura manuscrita. Para reportar una exactitud real se requiere un conjunto de prueba etiquetado, independiente y representativo.
