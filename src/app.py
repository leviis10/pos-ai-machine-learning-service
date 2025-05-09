import os
from flask import Flask
from src.config.database import db
from src.controller.optimal_price_controller import optimal_price_bp

app = Flask(__name__)

# Database Initialization
DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db.init_app(app)

# Routing
app.register_blueprint(optimal_price_bp)

def create_table():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
