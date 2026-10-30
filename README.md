# Reconocimiento inteligente de dígitos

## Archivos
- `index.html`: aplicación web autónoma, sin dependencias externas.

## Ejecutar localmente
1. Descarga y descomprime el proyecto.
2. Abre `index.html` en Chrome, Edge o Firefox.
3. Dibuja un dígito o carga una imagen y pulsa **Reconocer dígito**.
4. Ejecuta BFS, DFS, A* y el algoritmo genético desde sus botones.
5. Ejecuta las 25 pruebas sintéticas.

## Publicar en GitHub Pages
1. Crea un repositorio público en GitHub.
2. Sube `index.html` a la raíz del repositorio.
3. Abre **Settings → Pages**.
4. En **Build and deployment**, selecciona **Deploy from a branch**.
5. Selecciona la rama `main` y la carpeta `/ (root)`, guarda.
6. Espera a que GitHub Pages publique la URL.

## Alcance y limitaciones académicas
La aplicación utiliza prototipos tipográficos sencillos generados en el navegador y una extracción de rasgos explicable. No incorpora un modelo entrenado con MNIST ni garantiza reconocer escritura manuscrita arbitraria. Las 25 pruebas son sintéticas y sirven para comprobar el funcionamiento del flujo, no para afirmar rendimiento sobre datos reales. Para una evaluación rigurosa se debe usar un conjunto etiquetado independiente.
