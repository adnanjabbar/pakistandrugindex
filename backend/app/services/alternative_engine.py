def find_alternatives(brands, brand_id):
    target = next(b for b in brands if b["id"] == brand_id)

    return [
        b for b in brands
        if b["generic_id"] == target["generic_id"]
        and b["strength"] == target["strength"]
        and b["id"] != brand_id
    ]
