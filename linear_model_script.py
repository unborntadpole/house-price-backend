import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import root_mean_squared_error
import joblib

df = pd.read_csv("data_for_model.csv")

X = df.drop(columns=["flat_price"])
y = df["flat_price"]

categorical_cols = ["flat_type", "location1", "age_of_property", "furnishing", "parking"]
numerical_cols = ["buildupArea_sqft", "bedrooms", "bathrooms", "balcony"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

preds = pipeline.predict(X_test)
rmse = root_mean_squared_error(y_test, preds)
print(f"RMSE: {rmse:.3f} Lakhs")   # RMSE: 0.938 crores

joblib.dump(pipeline, "linear_model_pipeline.pkl")
