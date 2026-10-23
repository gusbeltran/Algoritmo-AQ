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
