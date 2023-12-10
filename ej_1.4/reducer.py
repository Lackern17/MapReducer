#!/usr/bin/python

import sys

maximoAbsoluto = 0

for line in sys.stdin:
    try:
        _, costo = line.strip().split("\t")
        costo = float(costo)

        # Actualizar el máximo absoluto
        maximoAbsoluto = max(maximoAbsoluto, abs(costo))

    except ValueError:
        # Manejar el caso en el que la conversión a flotante falla
        print("Saltando línea debido a datos inválidos:", line.strip())

# Imprimir el máximo absoluto de todas las ventas registradas
print(f"Maximo Absoluto:\t{maximoAbsoluto}")

