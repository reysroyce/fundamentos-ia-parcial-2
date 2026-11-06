# Actividad Integradora 3.1

## Tipos de aprendizaje automático

### Sección 1. Investigación --- 1.2 Clasificación del aprendizaje automático

**Tema:** Del dato al bien social: modelos de IA para transformar
realidades\
**Entrega:** Apartado 1.2 --- Clasificación y aplicaciones reales

------------------------------------------------------------------------

## 1.2 Clasificación del aprendizaje automático

### Introducción

El aprendizaje automático (*Machine Learning* o ML) se clasifica de
acuerdo con la forma en que un modelo recibe datos y retroalimentación
durante su entrenamiento. Los enfoques más conocidos son el aprendizaje
supervisado, no supervisado y por refuerzo. También existen el
semisupervisado y el aprendizaje por transferencia, que resultan útiles
en situaciones específicas \[1\]\[2\]\[3\].

La elección depende del problema, los datos disponibles y el resultado
esperado. Ningún enfoque es el mejor para todos los casos.

### 1.2.1 Aprendizaje supervisado

Utiliza datos etiquetados, es decir, ejemplos que incluyen información
de entrada y una respuesta correcta conocida. El algoritmo aprende la
relación entre ambos elementos para predecir resultados en datos nuevos
\[1\]\[2\].

Sus tareas principales son:

-   **Clasificación:** predice una categoría, por ejemplo, determinar si
    un correo es legítimo o no deseado.
-   **Regresión:** predice un valor numérico, por ejemplo, estimar el
    precio de una vivienda.

**Algoritmos representativos:** regresión lineal, regresión logística,
árboles de decisión, bosques aleatorios, máquinas de soporte vectorial
(SVM) y K vecinos más cercanos (KNN).

**Ventajas:** permite comparar predicciones con respuestas conocidas y
medir el desempeño.

**Limitaciones:** requiere datos etiquetados de calidad, cuya
preparación puede ser costosa o tardada.

### 1.2.2 Aprendizaje no supervisado

Trabaja con datos sin etiquetas. Su objetivo es encontrar estructuras,
similitudes, relaciones o patrones en la información \[1\]\[2\]\[3\].

Tareas frecuentes:

-   **Clustering o agrupamiento:** reúne datos similares, por ejemplo,
    clientes con hábitos de compra parecidos.
-   **Reglas de asociación:** encuentra elementos que suelen aparecer
    juntos, como productos comprados en una misma operación.
-   **Detección de anomalías:** identifica observaciones que se alejan
    del comportamiento habitual.
-   **Reducción de dimensionalidad:** representa los datos con menos
    variables, conservando información relevante.

**Algoritmos representativos:** K-Means, agrupamiento jerárquico,
DBSCAN, Apriori y análisis de componentes principales (PCA).

**Ventajas:** permite explorar datos sin etiquetar y descubrir patrones
no evidentes.

**Limitaciones:** los patrones encontrados necesitan interpretación y
validación; no todos los grupos serán útiles para el problema.

### 1.2.3 Aprendizaje por refuerzo

Un agente interactúa con un entorno, realiza acciones y recibe
recompensas o penalizaciones. Con esa retroalimentación aprende una
estrategia para maximizar la recompensa acumulada \[1\]\[2\]\[6\].

Elementos principales:

-   **Agente:** sistema que aprende y toma decisiones.
-   **Entorno:** espacio o sistema con el que interactúa.
-   **Estado:** situación actual del entorno.
-   **Acción:** decisión que realiza el agente.
-   **Recompensa:** señal que indica qué tan conveniente fue una acción.

**Algoritmos representativos:** Q-Learning, SARSA y métodos de gradiente
de política.

**Aplicaciones:** entrenamiento de agentes para juegos, control de
robots, navegación y optimización de decisiones secuenciales.

**Ventajas:** aprende comportamientos mediante la experiencia y la
retroalimentación.

**Limitaciones:** diseñar recompensas adecuadas puede ser difícil y el
entrenamiento puede requerir muchas interacciones y recursos de cómputo.

### 1.2.4 Aprendizaje semisupervisado

Combina una cantidad pequeña de datos etiquetados con una cantidad mayor
de datos sin etiquetar. Es útil cuando conseguir etiquetas es costoso o
requiere especialistas \[3\]\[7\].

**Ejemplo:** en el análisis de imágenes médicas, algunas imágenes pueden
estar anotadas por especialistas y muchas otras no. Un método
semisupervisado aprovecha ambos grupos durante el aprendizaje.

**Ventajas:** aprovecha datos sin etiquetar y puede reducir el trabajo
de clasificación manual.

**Limitaciones:** si las pocas etiquetas disponibles contienen errores o
los datos sin etiquetar son muy diferentes, el modelo puede aprender
patrones poco adecuados.

### 1.2.5 Aprendizaje por transferencia (*Transfer Learning*)

Consiste en aprovechar los conocimientos o parámetros de un modelo
previamente entrenado y adaptarlos a otra tarea relacionada. Es útil
cuando el nuevo problema tiene pocos datos o entrenar desde cero sería
costoso \[3\]\[8\].

**Ejemplo:** partir de un modelo entrenado para reconocer objetos en
fotografías y ajustarlo con imágenes de hojas para identificar
enfermedades de plantas.

**Ventajas:** puede reducir el tiempo de entrenamiento y la cantidad de
datos necesarios.

**Limitaciones:** funciona mejor cuando la tarea original y la nueva
están relacionadas. Si los datos son muy diferentes, el conocimiento
transferido podría no ser útil.

> **Nota:** el aprendizaje por transferencia no siempre se considera una
> categoría paralela a supervisado, no supervisado y por refuerzo. Es
> una estrategia para reutilizar conocimiento y puede combinarse con
> distintos enfoques \[3\]\[8\].

------------------------------------------------------------------------

## 1.2.6 Tabla comparativa de los tipos de aprendizaje automático

  ----------------------------------------------------------------------------------
  Tipo de           Datos          ¿Cómo aprende?  Tareas o           Ejemplo
  aprendizaje       utilizados                     algoritmos comunes 
  ----------------- -------------- --------------- ------------------ --------------
  Supervisado       Datos          Compara         Clasificación,     Clasificar
                    etiquetados    predicciones    regresión, KNN,    correos no
                                   con respuestas  SVM y árboles.     deseados.
                                   conocidas.                         

  No supervisado    Datos sin      Busca patrones, K-Means, DBSCAN,   Agrupar
                    etiquetas      grupos y        Apriori y PCA.     clientes por
                                   relaciones.                        hábitos.

  Por refuerzo      Interacción    Prueba acciones Q-Learning, SARSA  Enseñar a un
                    con un entorno y aprende de    y gradiente de     robot a
                    y recompensas  sus resultados. política.          realizar una
                                                                      tarea.

  Semisupervisado   Pocos datos    Combina ambos   Pseudoetiquetado y Analizar
                    etiquetados y  tipos de datos. métodos de         imágenes
                    muchos sin                     consistencia.      médicas con
                    etiquetar                                         pocas
                                                                      anotaciones.

  Por transferencia Modelo         Reutiliza y     Ajuste fino        Adaptar un
                    previamente    adapta          (*fine-tuning*) y  modelo de
                    entrenado y    conocimientos   extracción de      imágenes a
                    datos de una   aprendidos.     características.   fotografías de
                    nueva tarea                                       plantas.
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 1.2.7 Investigación de 10 aplicaciones reales del aprendizaje automático

La tabla reúne aplicaciones utilizadas o documentadas en distintos
sectores. La clasificación corresponde al enfoque que puede emplearse
para resolver cada tarea; una solución tecnológica completa puede
combinar más de un tipo de aprendizaje.

  ---------------------------------------------------------------------------------------
               Núm. Aplicación       Tipo de           ¿Cómo se utiliza? Beneficio o
                                     aprendizaje                         finalidad
  ----------------- ---------------- ----------------- ----------------- ----------------
                  1 Detección de     Supervisado ---   Se entrena con    Ayuda a reducir
                    correo no        clasificación     mensajes          mensajes no
                    deseado (*spam*)                   identificados     deseados.
                                                       como legítimos o  
                                                       no deseados para  
                                                       clasificar        
                                                       correos nuevos.   

                  2 Predicción del   Supervisado ---   Analiza ejemplos  Apoya la
                    precio de        regresión         históricos con    estimación de
                    viviendas                          características   precios según
                                                       de viviendas y    ubicación,
                                                       precios           tamaño y
                                                       conocidos.        antigüedad.

                  3 Análisis de      Supervisado ---   Aprende con       Apoya el
                    imágenes médicas clasificación o   imágenes anotadas análisis
                                     detección         para reconocer    clínico; no
                                                       patrones que      sustituye el
                                                       pueden ayudar a   diagnóstico
                                                       identificar       profesional.
                                                       hallazgos.        

                  4 Predicción de    Supervisado ---   Utiliza registros Contribuye a
                    condiciones      regresión         históricos y      elaborar
                    meteorológicas                     variables         pronósticos y
                                                       meteorológicas    apoyar la
                                                       para estimar      planificación.
                                                       valores futuros.  

                  5 Segmentación de  No supervisado    Agrupa clientes   Ayuda a
                    clientes         --- clustering    con               comprender
                                                       comportamientos   perfiles de
                                                       similares sin     consumidores.
                                                       asignarles        
                                                       categorías        
                                                       previamente.      

                  6 Detección de     No supervisado    Aprende patrones  Puede ayudar a
                    anomalías en     --- detección de  habituales de     detectar fallas
                    sensores         anomalías         funcionamiento y  y programar
                    industriales                       señala mediciones revisiones.
                                                       inusuales.        

                  7 Análisis de      No supervisado    Examina registros Apoya la
                    productos        --- reglas de     de compras para   organización de
                    comprados juntos asociación        encontrar         productos y el
                                                       productos que     análisis de
                                                       aparecen juntos   hábitos de
                                                       con frecuencia.   compra.

                  8 Clasificación de Semisupervisado   Aprovecha un      Reduce la
                    imágenes con                       grupo pequeño de  necesidad de
                    pocas etiquetas                    imágenes          etiquetar
                                                       etiquetadas y     manualmente
                                                       otro mayor sin    todos los
                                                       etiquetas.        ejemplos.

                  9 Aprendizaje de   Por refuerzo      Un agente prueba  Permite aprender
                    movimientos de                     acciones en un    estrategias para
                    robots                             entorno simulado  tareas de
                                                       o controlado y    manipulación o
                                                       recibe            control.
                                                       recompensas según 
                                                       el resultado.     

                 10 Adaptación de    Por transferencia Parte de un       Puede reducir el
                    modelos para                       modelo de         esfuerzo para
                    reconocer                          imágenes          desarrollar un
                    enfermedades de                    previamente       modelo
                    plantas                            entrenado y lo    especializado.
                                                       ajusta con        
                                                       fotografías del   
                                                       nuevo problema.   
  ---------------------------------------------------------------------------------------

### Comentario sobre las aplicaciones

Los ejemplos muestran que el aprendizaje automático tiene aplicaciones
en salud, comercio, meteorología, industria y robótica. La clasificación
depende de cómo se entrena el modelo y de la información que recibe. Por
ejemplo, el análisis de imágenes médicas puede ser supervisado cuando se
cuenta con imágenes etiquetadas, o semisupervisado cuando se combina un
grupo pequeño de imágenes anotadas con otro mayor sin anotaciones.

------------------------------------------------------------------------

## 1.2.8 Esquema general de clasificación

``` mermaid
flowchart TD
    A["Aprendizaje automático (ML)"]
    A --> B["Supervisado"]
    A --> C["No supervisado"]
    A --> D["Por refuerzo"]
    A --> E["Semisupervisado"]
    A --> F["Por transferencia"]

    B --> B1["Clasificación"]
    B --> B2["Regresión"]

    C --> C1["Clustering"]
    C --> C2["Reglas de asociación"]
    C --> C3["Reducción de dimensionalidad"]
    C --> C4["Detección de anomalías"]

    D --> D1["Agente"]
    D --> D2["Recompensas y penalizaciones"]
    D --> D3["Política de acciones"]

    E --> E1["Pocos datos etiquetados"]
    E --> E2["Muchos datos sin etiquetar"]

    F --> F1["Modelo previamente entrenado"]
    F --> F2["Adaptación a una nueva tarea"]
```

------------------------------------------------------------------------

## Conclusión

La clasificación del aprendizaje automático permite comprender que los
modelos no aprenden todos de la misma manera. El aprendizaje supervisado
utiliza ejemplos con respuestas conocidas; el no supervisado descubre
patrones en datos sin etiquetas; y el aprendizaje por refuerzo mejora
sus decisiones mediante recompensas o penalizaciones. El semisupervisado
combina datos etiquetados y no etiquetados, mientras que el aprendizaje
por transferencia reutiliza conocimientos de modelos previamente
entrenados.

Las diez aplicaciones investigadas muestran que estos enfoques pueden
ayudar a resolver problemas de diferentes sectores, como salud,
comercio, meteorología, industria y robótica. Para elegir un modelo
adecuado es necesario analizar el objetivo, la calidad y cantidad de los
datos, los recursos disponibles y los posibles riesgos de sus
resultados. Por ello, el aprendizaje automático debe desarrollarse y
utilizarse de manera responsable, con evaluación humana cuando sus
resultados puedan afectar a las personas.

------------------------------------------------------------------------

## Referencias bibliográficas (formato APA 7)

\[1\] Google for Developers. (s. f.). *What is machine learning?*
https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

\[2\] IBM. (s. f.). *What is machine learning?*
https://www.ibm.com/think/topics/machine-learning

\[3\] Mahesh, B. (2020). Machine learning algorithms---A review.
*International Journal of Science and Research (IJSR), 9*(1), 381--386.
https://pmc.ncbi.nlm.nih.gov/articles/PMC7983091/

\[4\] Google Cloud. (s. f.). *Supervised vs. unsupervised learning*.
https://cloud.google.com/discover/supervised-vs-unsupervised-learning

\[5\] International Organization for Standardization. (2021). *ISO/TR
24291:2021: Health informatics---Applications of machine learning
technologies in imaging and other medical applications*.
https://www.iso.org/standard/78345.html

\[6\] NVIDIA. (s. f.). *What is reinforcement learning?*
https://www.nvidia.com/en-us/glossary/reinforcement-learning/

\[7\] Amazon Web Services. (s. f.). *What is supervised learning?*
https://aws.amazon.com/what-is/supervised-learning/

\[8\] Stanford University, CS229. (2021). *Types of learning* \[Apuntes
de clase\].
https://cs229.stanford.edu/notes2021fall/lecture14-types-of-learning-annotated.pdf

**Fecha de consulta:** 6 de noviembre de 2026.

------------------------------------------------------------------------

## Declaración de uso de inteligencia artificial

Para la elaboración de este apartado se utilizó ChatGPT (OpenAI) como
herramienta de apoyo para organizar la información, explicar los tipos
de aprendizaje automático, estructurar la tabla de aplicaciones y
mejorar la redacción. Se consultaron las fuentes bibliográficas
incluidas en el documento. El contenido debe ser revisado y comprendido
por el estudiante antes de su entrega.

------------------------------------------------------------------------

**Fin del apartado 1.2 --- Clasificación del aprendizaje automático.**
