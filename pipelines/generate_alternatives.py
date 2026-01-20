def generate_alternatives(brands):
    alternatives = []
    for b in brands:
        for other in brands:
            if (
                b["generic_id"] == other["generic_id"]
                and b["strength"] == other["strength"]
                and b["id"] != other["id"]
            ):
                alternatives.append({
                    "brand_id": b["id"],
                    "alternative_brand_id": other["id"],
                    "reason": "Same generic and strength"
                })
    return alternatives
