import matplotlib.pyplot as plt

# DATOS


positivos = [
    {"edad": 25, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 32, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 45, "frecuencia": "frecuente", "plan": "premium"}
]

negativos = [
    {"edad": 25, "frecuencia": "ocasional", "plan": "basico"},
    {"edad": 32, "frecuencia": "ocasional", "plan": "estandar"},
    {"edad": 38, "frecuencia": "rara", "plan": "basico"}
]

# DESCUBRIR ATRIBUTOS

atributos = list(positivos[0].keys())

print("Atributos detectados:")
print(atributos)

# BUSCAR REGLAS CANDIDATAS


reglas = []

for atributo in atributos:

    valores_positivos = {
        ejemplo[atributo]
        for ejemplo in positivos
    }

    valores_negativos = {
        ejemplo[atributo]
        for ejemplo in negativos
    }

    exclusivos = valores_positivos - valores_negativos

    for valor in exclusivos:
        reglas.append({
            "atributo": atributo,
            "valor": valor
        })


# MOSTRAR REGLAS ENCONTRADAS

print("\nREGLAS CANDIDATAS\n")

for regla in reglas:
    print(
        f"SI {regla['atributo']} = {regla['valor']} "
        f"ENTONCES Socio_Activo = SI"
    )

# ==========================
# EVALUAR REGLAS
# ==========================

print("\nEVALUACION\n")

for regla in reglas:

    atributo = regla["atributo"]
    valor = regla["valor"]

    positivos_ok = sum(
        1 for x in positivos
        if x[atributo] == valor
    )

    negativos_ok = sum(
        1 for x in negativos
        if x[atributo] == valor
    )

    print(
        f"{atributo} = {valor}"
        f" | Positivos cubiertos: {positivos_ok}/{len(positivos)}"
        f" | Negativos cubiertos: {negativos_ok}/{len(negativos)}"
    )



# GRAFICO DE IMPORTANCIA


variables = [
    "Frecuencia de asistencia",
    "Plan contratado",
    "Edad del socio"
]

importancia = [100, 100, 33]

plt.figure(figsize=(9, 5))

barras = plt.bar(
    variables,
    importancia,
    color=["green", "green", "orange"]
)

plt.title(
    "Factores que ayudan a identificar un socio activo"
)

plt.ylabel("Capacidad predictiva (%)")

plt.ylim(0, 110)

for barra in barras:

    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 2,
        f"{altura:.0f}%",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.show()
plt.show()
