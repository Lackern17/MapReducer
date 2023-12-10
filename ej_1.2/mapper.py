#!/usr/bin/python

import sys

for line in sys.stdin:
    try:
        # Format of each line is: date\ttime\tstore name\titem description\tcost\tmethod of payment
        data = line.strip().split("\t")
        
        if len(data) == 6:
            # Extract relevant information
            category, cost = data[3], data[4]
            
            # Print to standard output
            print(f"{category}\t{cost}")

    except ValueError:
        # Handle the case where conversion to float fails
        print("Skipping line due to invalid data:", line.strip())
