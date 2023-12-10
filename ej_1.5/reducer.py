#!/usr/bin/python

import sys

totalVentas = 0

for line in sys.stdin:
    try:
        _, costo = line.strip().split("\t")
        costo = float(costo)

        # Sumar al total de ventas
        totalVentas += costo

    except ValueError:
        # Manejar el caso en el que la conversión a flotante falla
        print("Saltando línea debido a datos inválidos:", line.strip())

# Imprimir el total de ventas
print(f"Total de Ventas:\t{totalVentas}")

