Algoritmo AQ: Compra de Autos Eléctricos
Descripción

Este proyecto implementa una versión simplificada del algoritmo AQ, un método de aprendizaje inductivo basado en reglas. El objetivo es identificar las características que distinguen a los clientes que compran vehículos eléctricos de aquellos que no realizan esta compra.

Se utiliza un conjunto de ejemplos positivos (clientes compradores) y negativos (clientes no compradores), considerando atributos como:

Edad
Nivel de ingresos
Disponibilidad de garaje
Distancia al trabajo

El algoritmo analiza los ejemplos para encontrar atributos que permitan generar reglas de clasificación.

Objetivo

Descubrir patrones que expliquen por qué ciertos clientes adquieren vehículos eléctricos y construir una regla capaz de diferenciarlos de quienes no los compran.

Resultados

Tras comparar los ejemplos positivos y negativos, se observa que todos los compradores poseen garaje, mientras que ninguno de los ejemplos negativos cuenta con esta característica.

La regla inducida es:

SI tiene_garaje = "Si"
ENTONCES comprador_auto_electrico = SI

Conclusión

El análisis muestra que la disponibilidad de un garaje es el atributo más determinante para identificar potenciales compradores de vehículos eléctricos dentro del conjunto de datos utilizado. Esto tiene sentido porque la mayoría de los propietarios de autos eléctricos necesitan un espacio adecuado para la instalación y uso de sistemas de carga en el hogar. El algoritmo AQ logró descubrir esta regla de manera automática a partir de ejemplos positivos y negativos, demostrando cómo los sistemas de aprendizaje basado en reglas pueden extraer conocimiento útil a partir de datos simples.

Algoritmo AQ: Identificación de Socios Activos de Gimnasio
Descripción

Este proyecto utiliza una implementación sencilla del algoritmo AQ para descubrir qué características permiten identificar a los socios más activos de un gimnasio.

El conjunto de datos está compuesto por ejemplos positivos (socios activos) y negativos (socios poco activos o inactivos). Cada socio se describe mediante:

Edad
Frecuencia de asistencia
Tipo de plan contratado

El algoritmo busca valores que aparezcan exclusivamente en los socios activos y genera reglas predictivas a partir de ellos.

Objetivo

Determinar qué variables poseen mayor capacidad para distinguir a los socios activos de los no activos y generar reglas de clasificación interpretables.

Resultados

El análisis encontró que los socios activos presentan principalmente dos características:

SI frecuencia = frecuente
ENTONCES Socio_Activo = SI


y

SI plan = premium
ENTONCES Socio_Activo = SI


Además, el gráfico generado muestra el nivel de importancia de las variables analizadas:

Frecuencia de asistencia: 100%
Plan contratado: 100%
Edad: 33%

Esto indica que la edad posee una capacidad predictiva mucho menor respecto de las otras variables.

Conclusión

Los resultados demuestran que la frecuencia de asistencia y el tipo de plan contratado son los mejores indicadores para identificar a un socio activo. La edad, aunque puede aportar cierta información, no resulta suficiente para distinguir claramente entre socios activos e inactivos. El algoritmo AQ permitió descubrir reglas simples y fácilmente interpretables, mostrando cómo el aprendizaje basado en reglas puede utilizarse para apoyar la toma de decisiones en entornos de gestión deportiva y análisis de clientes.
