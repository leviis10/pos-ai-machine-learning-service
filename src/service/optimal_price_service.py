from src.model.optimal_prices import OptimalPrices
from src.repository.optimal_price_repository import OptimalPriceRepository
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.linear_model import LinearRegression

class OptimalPriceService:
    @staticmethod
    def predict_optimal_price(user_id, request):
        foundOptimalPrices = OptimalPriceRepository.get_all_by_user_id(user_id)

        data = [
            {column.name: getattr(row, column.name) for column in row.__table__.columns}
            for row in foundOptimalPrices
        ]
        dataset = pd.DataFrame(data)
        dataset = dataset.drop('id', axis=1)
        dataset = dataset.drop('user_id', axis=1)

        X = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]

        ct = ColumnTransformer(
            transformers = [("encoder", OneHotEncoder(drop="first"), ["product_category", "product_type"])],
            remainder = "passthrough"
        )
        X = np.array(ct.fit_transform(X))

        regressor = LinearRegression()
        regressor.fit(X, y)

        request_data = pd.DataFrame([request])
        request_data = request_data[dataset.columns[:-1]]
        X_request = np.array(ct.transform(request_data))
        predicted_price = regressor.predict(X_request)
        print(predicted_price)

        return {
            "productCategory": request["product_category"],
            "buyingPrice": request["buying_price"],
            "buyQuantity": request["buy_quantity"],
            "productType": request["product_type"],
            "optimalPrice": predicted_price[0],
            "userId": user_id
        }