# GRAFO REPRESENTATIVO PARA RECONOCIMIENTO DE DÍGITOS

## Objetivo
Representar mediante un grafo el proceso de reconocimiento de números del 0 al 9.

## Nodos
- Unknown (imagen desconocida).
- Análisis de píxeles.
- Huecos.
- Líneas.
- Curvas.
- Simetría.
- Dígitos del 0 al 9.

## Aristas y pesos

| Conexión | Peso |
|---|---:|
| Unknown → Análisis | 1 |
| Análisis → Huecos | 2 |
| Análisis → Líneas | 2 |
| Análisis → Curvas | 3 |
| Análisis → Simetría | 2 |
| Huecos → 0 | 1 |
| Huecos → 8 | 2 |
| Líneas → 1 | 1 |
| Líneas → 7 | 2 |
| Curvas → 3 | 2 |
| Curvas → 6 | 2 |
| Curvas → 9 | 2 |
| Simetría → 8 | 1 |

## Representación del grafo

Unknown
   |
Análisis de píxeles
   |
   |--- Huecos → 0, 8
   |--- Líneas → 1, 7
   |--- Curvas → 3, 6, 9
   |--- Simetría → 8

## Conclusión
El grafo permite analizar las características de una imagen y encontrar el dígito que tenga mayor similitud.
