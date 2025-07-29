from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

linear_regression_pipeline = joblib.load("linear_model_pipeline.pkl")
clusters_df = pd.read_csv("data_with_clusters.csv")

app = FastAPI(title="Mumbai Housing Price Predictor 🏠")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HouseFeatures(BaseModel):
    flat_type: str
    location1: str
    age_of_property: str
    furnishing: str
    parking: str
    buildupArea_sqft: float
    bedrooms: int
    bathrooms: int
    balcony: int

@app.get("/")
def read_root():
    return {"message": "🏙️ Welcome to the Mumbai Housing API!"}

@app.post("/predict")
def predict_price(data: HouseFeatures):
    input_df = pd.DataFrame([data.dict()])
    prediction = linear_regression_pipeline.predict(input_df)[0]
    return {"predicted_price_lakhs": round(prediction, 2)}

@app.get("/clusters")
def get_clusters():
    summary = clusters_df.groupby("cluster")["location1"].value_counts().reset_index(name="count")
    return summary.to_dict(orient="records")
