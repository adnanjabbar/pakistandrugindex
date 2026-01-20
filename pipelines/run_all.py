from load_csv import load_csv
from generate_alternatives import generate_alternatives

brands = load_csv("data/brands/brands.csv")
alternatives = generate_alternatives(brands)

print(f"Generated {len(alternatives)} alternatives")
