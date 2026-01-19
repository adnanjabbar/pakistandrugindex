def calculate_trend(price_history):
    if len(price_history) < 2:
        return "stable"
    return "increasing" if price_history[-1]["price_pkr"] > price_history[0]["price_pkr"] else "decreasing"
