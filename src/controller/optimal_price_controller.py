from flask import Blueprint, request, jsonify
from src.service.optimal_price_service import OptimalPriceService

optimal_price_bp = Blueprint("optimal_price", __name__, url_prefix="/machine-learning-service/api/v1/optimal-price")

@optimal_price_bp.route("/predict", methods=["GET"])
def predict_optimal_price():
    req = request.get_json()
    mapped_req = {}
    mapped_req["product_category"] = req["productCategory"]
    mapped_req["buying_price"] = req["buyingPrice"]
    mapped_req["buy_quantity"] = req["buyQuantity"]
    mapped_req["product_type"] = req["productType"]
    user_id = request.headers.get("User-ID")
    res = OptimalPriceService.predict_optimal_price(user_id, mapped_req)
    return jsonify(res), 200