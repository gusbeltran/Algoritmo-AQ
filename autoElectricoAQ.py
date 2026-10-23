# Ejemplo de implementación simple del algoritmo AQ
# Caso: concesionaria que quiere identificar clientes que compran autos eléctricos

# Ejemplos positivos (+)
positivos = [
    {"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Corta"}, #j0
    {"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "Si", "distancia_trabajo": "Media"},# j1
    {"edad": "Mayor", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Larga"}# j2
]

# Ejemplos negativos (-)
negativos = [
    {"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "No", "distancia_trabajo": "Corta"},
    {"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "No", "distancia_trabajo": "Media"},
    {"edad": "Mayor", "ingreso": "Bajo", "tiene_garaje": "No", "distancia_trabajo": "Larga"}
]

# Paso 1: identificar atributos comunes en positivos
def atributos_comunes(positivos):
    comunes = {}
    # Recorremos cada atributo del primer ejemplo
    for i in positivos[0].keys():
        valores = []
        # Guardamos los valores de ese atributo en todos los positivos
        for j in positivos:
            valores.append(j[i])
        
        # Verificamos si todos los valores son iguales
        todos_iguales = True
        for v in valores:
            if v != valores[0]:
                todos_iguales = False
                break
        
        # Si son iguales, lo agregamos al diccionario de comunes
        if todos_iguales:
            comunes[i] = valores[0]
            fin =  print(valores)
    
    return fin

atributos_comunes
"""
# Paso 2: verificar que el atributo distingue positivos de negativos
def verificar_regla(regla, positivos, negativos):
    # La regla es un diccionario con condiciones
    for ej in positivos:
        if not all(ej[attr] == val for attr, val in regla.items()):
            return False
    for ej in negativos:
        if all(ej[attr] == val for attr, val in regla.items()):
            return False
    return True

# Aplicación del algoritmo AQ
regla_inducida = {"tiene_garaje": "Si"}

# Verificación
es_valida = verificar_regla(regla_inducida, positivos, negativos)

print("Regla inducida:", regla_inducida)
print("¿La regla es válida?:", es_valida)

# Resultado esperado:
# Regla inducida: {'tiene_garaje': 'Si'}
# ¿La regla es válida?: True
"""