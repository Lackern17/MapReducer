#!/usr/bin/python

import sys

ventaMasAltaPorMetodo = {}

for line in sys.stdin:
    try:
        metodoPago, costo = line.strip().split("\t")
        costo = float(costo)

        # Actualizar la venta más alta para el método de pago actual
        if metodoPago in ventaMasAltaPorMetodo:
            ventaMasAltaPorMetodo[metodoPago] = max(ventaMasAltaPorMetodo[metodoPago], costo)
        else:
            ventaMasAltaPorMetodo[metodoPago] = costo

    except ValueError:
        # Manejar el caso en el que la conversión a flotante falla
        print("Saltando línea debido a datos inválidos:", line.strip())

# Imprimir la venta más alta para cada método de pago
for metodoPago, ventaMasAlta in ventaMasAltaPorMetodo.items():
    print(f"{metodoPago}\t{ventaMasAlta}")

