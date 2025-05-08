from flask import Blueprint, request, jsonify
from src.service.sales_service import SalesService

sales_bp = Blueprint("currents", __name__, url_prefix="/machine-learning-service/api/v1/sales")

@sales_bp.route("/add-sold-count", methods=["POST"])
def add_sold_count():
    data = request.get_json()
    user_id = request.headers.get("User-ID")
    sales = SalesService.add_sold_count(user_id, data)
    return jsonify(sales, 200)