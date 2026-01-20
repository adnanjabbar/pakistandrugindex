import csv

DATA_PATH = "data/brands/brands.csv"

def load_brands():
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
