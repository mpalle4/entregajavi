# tests/test_utils.py
from utils import calculate_top_sellers, summarize_sales

def test_calculate_top_sellers_basic():
    sales = [("a", 2), ("b", 3), ("a", 1)]
    res = calculate_top_sellers(sales, top_n=2)
    assert res[0][0] == "b" or res[0][0] == "a"  # orden según cantidades

def test_summarize_sales_empty():
    res = summarize_sales([])
    assert res["total_items"] == 0
    assert res["unique_products"] == 0
    assert res["average_per_product"] == 0
