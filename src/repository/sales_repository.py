from src.model.sales import Sales

class SalesRepository:
    @staticmethod
    def save(sales):
        sales.save()
        return sales
    
    @staticmethod
    def find_all():
        return Sales.objects.all()
    
    @staticmethod
    def find_by_product_category_and_product_price_and_promo_applied_and_day_of_week_and_is_holiday_and_created_at_and_user_id(
        product_category,
        product_price,
        promo_applied,
        day_of_week,
        is_holiday,
        created_at,
        user_id
    ):
        return Sales.objects(
            product_category=product_category,
            product_price=product_price,
            promo_applied=promo_applied,
            day_of_week=day_of_week,
            is_holiday=is_holiday,
            created_at=created_at,
            user_id=user_id
        ).first()