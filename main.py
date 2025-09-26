# main.py
from utils import calculate_top_sellers, summarize_sales
import json

if __name__ == "__main__":
    # ejemplo de datos de input
    sales = [
        ("remera", 10),
        ("jeans", 5),
        ("zapatillas", 12),
        ("buzo", 4),
        ("remera", 7),
        ("jeans", 3),
        ("zapatillas", 8),
        ("remera", 2),
    ]

    top3 = calculate_top_sellers(sales, top_n=3)
    summary = summarize_sales(sales)

    print("Top 3 productos vendidos:")
    for prod, qty in top3:
        print(f"- {prod}: {qty}")

    print("\nResumen general:")
    print(json.dumps(summary, indent=2))
