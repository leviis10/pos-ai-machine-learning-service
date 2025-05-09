from src.model.optimal_prices import OptimalPrices

class OptimalPriceRepository:
    @staticmethod
    def get_all_by_user_id(user_id):
        return OptimalPrices.query.filter_by(user_id=user_id).all()