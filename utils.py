# utils.py
from collections import Counter
from typing import List, Tuple, Dict, Iterator

def _normalize_sales(sales: List[Tuple[str, int]]) -> Iterator[Tuple[str, int]]:
    """
    Valida y convierte las tuplas de ventas a (item, int(qty)).
    Lanza ValueError si una tupla no tiene forma correcta o qty no es convertible.
    """
    for entry in sales:
        if not (isinstance(entry, (list, tuple)) and len(entry) == 2):
            raise ValueError(f"Cada venta debe ser una tupla (item, qty). Entrada inválida: {entry}")
        item, qty = entry
        try:
            qty_int = int(qty)
        except (TypeError, ValueError):
            raise ValueError(f"Cantidad no convertible a int: {qty!r} para item {item!r}")
        yield item, qty_int

def calculate_top_sellers(sales: List[Tuple[str, int]], top_n: int = 3) -> List[Tuple[str, int]]:
    """
    Recibe una lista de tuplas (item, cantidad) y devuelve los top_n productos con la suma de cantidades.
    """
    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n debe ser un entero positivo")

    counter = Counter()
    for item, qty in _normalize_sales(sales):
        counter[item] += qty

    return counter.most_common(top_n)

def summarize_sales(sales: List[Tuple[str, int]]) -> Dict:
    """
    Devuelve un resumen: total_items, productos_unicos, total_cantidad, por_producto.
    """
    counter = Counter()
    for item, qty in _normalize_sales(sales):
        counter[item] += qty

    total = sum(counter.values())
    unique = len(counter)

    return {
        "total_items": total,
        "unique_products": unique,
        "total_quantity": total,
        "by_product": dict(counter)
    }
