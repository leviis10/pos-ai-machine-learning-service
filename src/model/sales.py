from src.config.database import db

class Sales(db.Document):
    product_category = db.StringField(required=True)
    product_price = db.DecimalField(required=True)
    promo_applied = db.StringField(required=True)
    day_of_week = db.StringField(required=True)
    is_holiday = db.BooleanField(required=True)
    created_at = db.DateField(required=True)
    user_id = db.IntField(required=True)
    sold_count = db.IntField(required=True)