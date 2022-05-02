import csv
import os
from pathlib import Path

def read_data(file):
    output = []
    with open(file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output.append(row)
    return output
