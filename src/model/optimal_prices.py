from src.config.database import db

class OptimalPrices(db.Model):
    __tablename__ = 'optimal_prices'

    id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String(255))
    buying_price = db.Column(db.Float)
    buy_quantity = db.Column(db.Integer)
    product_type = db.Column(db.String(255))
    optimal_price = db.Column(db.Float)
    user_id = db.Column(db.Integer)
