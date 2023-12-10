#!/usr/bin/python

import sys

totalSales = 0
oldCategory = None

for line in sys.stdin:
    try:
        category, cost = line.strip().split("\t")
        cost = float(cost)

        # Write a category:total_sales pair on a category change
        # Reset the total
        if oldCategory and oldCategory != category:
            print(f"{oldCategory}\t{totalSales}")
            oldCategory = category
            totalSales = 0

        oldCategory = category
        totalSales += cost

    except ValueError:
        # Handle the case where conversion to float fails
        print("Skipping line due to invalid data:", line.strip())

# Write the last pair once the loop is finished
if oldCategory is not None:
    print(f"{oldCategory}\t{totalSales}")
