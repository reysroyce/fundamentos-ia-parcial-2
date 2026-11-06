# Actividad Integradora 3.1

## Tipos de aprendizaje automático

### Sección 1. Investigación --- 1.1 Investigación conceptual

> **Tema:** Del dato al bien social: modelos de IA para transformar
> realidades\
> **Apartado:** 1.1 --- Concepto de aprendizaje automático y conceptos
> fundamentales

------------------------------------------------------------------------

## 1.1.1 Concepto de aprendizaje automático

El aprendizaje automático (*Machine Learning* o ML) es una rama de la
inteligencia artificial que desarrolla métodos para que los sistemas
informáticos identifiquen patrones a partir de datos y utilicen lo
aprendido para realizar predicciones o tomar decisiones. En lugar de
programar manualmente una regla para cada situación, se entrena un
modelo con ejemplos para que pueda generalizar a datos nuevos
\[1\]\[2\].

En términos sencillos, el aprendizaje automático permite que una
computadora encuentre relaciones dentro de la información y aproveche
esas relaciones para resolver tareas, como clasificar imágenes,
reconocer mensajes no deseados o estimar valores.

### Definiciones de fuentes confiables

**Definición 1 --- Google for Developers.** Google explica que el
aprendizaje automático es una forma de entrenar un modelo para realizar
predicciones o generar contenido a partir de datos, en lugar de
programar explícitamente todas las reglas de la tarea \[1\].

**Definición 2 --- IBM.** IBM describe el aprendizaje automático como
una rama de la inteligencia artificial que utiliza datos y algoritmos
para imitar la manera en que las personas aprenden, mejorando
gradualmente su precisión \[2\].

### Definición propia

El aprendizaje automático es una tecnología que permite a una
computadora analizar ejemplos, reconocer patrones y utilizar esa
información para generar resultados. El sistema aprende durante un
proceso de entrenamiento y después puede aplicar lo aprendido a
información nueva, aunque su desempeño depende de la calidad de los
datos y de cómo se haya construido y evaluado el modelo.

### ¿Para qué sirve el aprendizaje automático?

Se utiliza en diferentes actividades de la vida cotidiana y en sectores
profesionales. Algunos ejemplos son:

-   **Filtrado de correo no deseado:** ayuda a distinguir mensajes
    legítimos de posibles correos spam.
-   **Sistemas de recomendación:** sugieren películas, música, videos o
    productos según patrones de uso.
-   **Reconocimiento de imágenes:** identifica objetos, animales o
    elementos en fotografías.
-   **Detección de operaciones inusuales:** señala transacciones que
    podrían requerir una revisión adicional.
-   **Predicción:** estima valores futuros utilizando información
    histórica.

------------------------------------------------------------------------

## 1.1.2 Diferencias entre programación tradicional y aprendizaje automático

La programación tradicional y el aprendizaje automático son dos formas
de resolver problemas con computadoras, pero se diferencian en la manera
en que se define la solución.

En la **programación tradicional**, el desarrollador escribe
instrucciones y reglas que la computadora debe seguir. El programa
procesa los datos conforme a esas reglas y produce un resultado.

En el **aprendizaje automático**, se proporcionan ejemplos a un
algoritmo para que ajuste un modelo y encuentre patrones. Una vez
entrenado, el modelo utiliza esos patrones para realizar predicciones
sobre datos nuevos \[1\]\[2\].

### Tabla comparativa

  -----------------------------------------------------------------------
  Aspecto                 Programación            Aprendizaje automático
                          tradicional             
  ----------------------- ----------------------- -----------------------
  Cómo funciona           El programador define   El algoritmo aprende
                          las reglas y las        patrones a partir de
                          instrucciones.          ejemplos.

  Papel de los datos      Los datos se procesan   Los datos se utilizan
                          siguiendo reglas        para entrenar, validar
                          previamente escritas.   y probar el modelo.

  Modificación            Para cambiar el         El modelo puede volver
                          comportamiento          a entrenarse con datos
                          normalmente se          adecuados.
                          modifican las reglas o  
                          el código.              

  Uso adecuado            Problemas con pasos y   Problemas donde es útil
                          reglas claramente       identificar patrones
                          establecidos.           difíciles de describir
                                                  manualmente.

  Ejemplo                 Una calculadora que     Un filtro que aprende a
                          ejecuta operaciones     clasificar correos no
                          programadas.            deseados.
  -----------------------------------------------------------------------

### Ejemplo práctico: identificar correo no deseado

Imaginemos que se desea crear un sistema para separar correos legítimos
de mensajes no deseados.

-   **Con programación tradicional:** el desarrollador establece reglas,
    por ejemplo, revisar determinadas palabras o condiciones del
    remitente. El sistema aplica esas reglas a cada mensaje.
-   **Con aprendizaje automático:** se reúnen muchos correos previamente
    clasificados como legítimos o no deseados. El algoritmo analiza sus
    características y entrena un modelo para clasificar mensajes nuevos.

El segundo enfoque puede reconocer combinaciones de patrones que no
fueron escritas manualmente como reglas individuales. Sin embargo,
necesita datos representativos y una evaluación adecuada para evitar
errores.

------------------------------------------------------------------------

## 1.1.3 Conceptos fundamentales: dataset, etiqueta, feature y función de pérdida

Estos conceptos ayudan a comprender cómo se organiza la información que
utiliza un modelo y cómo se mide el resultado de su entrenamiento
\[3\]\[4\].

### a) Dataset (conjunto de datos)

Es una colección organizada de ejemplos o registros que se utiliza para
analizar información y, según el propósito, entrenar, validar o probar
un modelo de aprendizaje automático. Puede contener números, texto,
imágenes, sonidos u otros tipos de información.

**Ejemplo:** un conjunto de fotografías de perros y gatos que se utiliza
para entrenar un modelo que aprenda a distinguir entre ambos animales.

### b) Etiqueta (label)

Es la respuesta correcta o categoría asociada a un ejemplo. En el
aprendizaje supervisado, las etiquetas sirven para que el modelo compare
sus predicciones con los resultados conocidos durante el entrenamiento.

**Ejemplo:** si una fotografía contiene un perro, su etiqueta puede ser
"perro"; si contiene un gato, su etiqueta puede ser "gato".

### c) Feature (característica)

Es una variable o atributo de entrada que utiliza el modelo para
identificar patrones y generar predicciones. Las características
representan información relevante de cada ejemplo.

**Ejemplo:** para clasificar animales mediante fotografías, algunas
características visuales pueden ser la forma de las orejas, el tamaño,
el color o los patrones del pelaje.

### d) Función de pérdida (loss function)

Es una función matemática que mide la diferencia entre la predicción del
modelo y el resultado esperado. Durante el entrenamiento, el algoritmo
utiliza esa medida para ajustar los parámetros del modelo y,
normalmente, intenta reducir el valor de la pérdida. La función concreta
depende del tipo de problema \[3\]\[4\].

**Ejemplo:** si un modelo predice "perro" para una fotografía cuya
etiqueta correcta es "gato", la función de pérdida calcula un valor que
representa el error de esa predicción.

### Ejemplo integrador de los cuatro conceptos

Imaginemos que se construye un modelo para reconocer perros y gatos a
partir de fotografías:

  -----------------------------------------------------------------------
  Concepto                            Ejemplo
  ----------------------------------- -----------------------------------
  Dataset                             Colección de fotografías de perros
                                      y gatos.

  Etiqueta                            La categoría correcta de cada
                                      fotografía: "perro" o "gato".

  Feature                             Características visuales que el
                                      modelo utiliza, como formas,
                                      patrones o colores.

  Función de pérdida                  Medida matemática del error entre
                                      la predicción y la etiqueta
                                      correcta.
  -----------------------------------------------------------------------

En este ejemplo, el dataset contiene los casos de entrenamiento; las
etiquetas indican la respuesta esperada; las features aportan
información para distinguir los animales; y la función de pérdida
permite medir qué tan equivocadas son las predicciones durante el
entrenamiento.

------------------------------------------------------------------------

## Conclusión

El aprendizaje automático es una parte importante de la inteligencia
artificial porque permite que los sistemas informáticos aprendan
patrones a partir de datos y utilicen ese conocimiento para realizar
predicciones. Se diferencia de la programación tradicional porque el
comportamiento del modelo se obtiene mediante un proceso de
entrenamiento con ejemplos, en lugar de depender exclusivamente de
reglas escritas para cada caso.

También es importante comprender los conceptos de dataset, etiqueta,
feature y función de pérdida, ya que explican cómo se organiza la
información, qué intenta predecir el modelo y cómo se mide el error
durante su entrenamiento. Estos fundamentos permiten entender mejor las
aplicaciones del aprendizaje automático y reconocer que sus resultados
dependen de la calidad de los datos y de una evaluación responsable.

------------------------------------------------------------------------

## Referencias bibliográficas (formato APA 7)

\[1\] Google for Developers. (s. f.). *What is machine learning?*
https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

\[2\] IBM. (s. f.). *What is machine learning?*
https://www.ibm.com/think/topics/machine-learning

\[3\] Google for Developers. (s. f.). *Machine learning glossary: ML
fundamentals*.
https://developers.google.com/machine-learning/glossary/fundamentals

\[4\] Google for Developers. (s. f.). *Machine learning glossary*.
https://developers.google.com/machine-learning/glossary

**Fecha de consulta:** 6 de noviembre de 2026.

------------------------------------------------------------------------

## Declaración de uso de inteligencia artificial

Para la elaboración de este apartado se utilizó ChatGPT (OpenAI) como
herramienta de apoyo para organizar la información, aclarar conceptos y
mejorar la redacción. Se consultaron las fuentes bibliográficas
incluidas en el documento. El estudiante debe revisar y comprender el
contenido antes de presentarlo.

------------------------------------------------------------------------

**Fin del apartado 1.1 --- Investigación conceptual.**
