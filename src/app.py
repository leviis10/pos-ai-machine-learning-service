import os
from flask import Flask
from config.database import db
from src.controller.sales_controller import sales_bp

app = Flask(__name__)

# Database Initialization
DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
app.config["MONGODB_SETTINGS"] = {
    "db": DB_NAME,
    "host": DB_HOST,
    "port": DB_PORT
}
db.init_app(app)

# Routing
app.register_blueprint(sales_bp)

if __name__ == '__main__':
    app.run(debug=True)
