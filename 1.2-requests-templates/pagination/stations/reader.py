import csv
import os
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')


def read_data(file):
    output = []
    with open(file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output.append(row)
    return output
