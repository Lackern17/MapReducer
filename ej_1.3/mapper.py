#!/usr/bin/python

import sys

for line in sys.stdin:
    try:
        # El formato de cada línea es: fecha\thora\nombre de la tienda\descripción del artículo\costo\método de pago
        data = line.strip().split("\t")
        
        if len(data) == 6:
            # Extraer la información relevante
            metodoPago, costo = data[5], data[4]
            
            # Imprimir en la salida estándar
            print(f"{metodoPago}\t{costo}")

    except ValueError:
        # Manejar el caso en el que la conversión a flotante falla
        print("Saltando línea debido a datos inválidos:", line.strip())

