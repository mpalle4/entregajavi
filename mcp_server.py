# mcp_server.py
from flask import Flask, jsonify, request
from utils import summarize_sales, calculate_top_sellers

app = Flask(__name__)

# endpoint para obtener resumen de ventas (simula herramienta MCP)
@app.route("/get_sales_summary", methods=["POST"])
def get_sales_summary():
    data = request.get_json() or {}
    sales = data.get("sales", [])
    top_n = data.get("top_n", 3)
    summary = summarize_sales(sales)
    top = calculate_top_sellers(sales, top_n=top_n)
    return jsonify({"summary": summary, "top": top})

# endpoint para ejecutar tests (simulado)
@app.route("/run_tests", methods=["GET"])
def run_tests():
    # en un servidor real, podríamos ejecutar pytest y devolver resultados
    return jsonify({"status": "ok", "message": "tests simulated - run pytest locally for full report"})

if __name__ == "__main__":
    app.run(port=5000)
