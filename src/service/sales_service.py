from src.model.sales import Sales
from src.repository.sales_repository import SalesRepository

class SalesService:
    @staticmethod
    def create(user_id, request):
        newSales = Sales(
            product_category=request["product_category"],
            product_price=request["product_price"],
            promo_applied=request["promo_applied"],
            day_of_week=request["day_of_week"],
            is_holiday=request["is_holiday"],
            user_id=user_id,
            sold_count=request["sold_count"]
        )
        return SalesRepository.save(newSales)
    
    @staticmethod
    def add_sold_count(user_id,request):
        found_sales = SalesRepository.find_by_product_category_and_product_price_and_promo_applied_and_day_of_week_and_is_holiday_and_created_at_and_user_id(
            product_category=request["product_category"],
            product_price=request["product_price"],
            promo_applied=request["promo_applied"],
            day_of_week=request["day_of_week"],
            is_holiday=request["is_holiday"],
            created_at=request["created_at"],
            user_id=user_id
        )

        if found_sales:
            found_sales.sold_count += request["sold_count"]
            found_sales = SalesRepository.save(found_sales)
        else:
            found_sales = SalesService.create(user_id, request)

        return found_sales