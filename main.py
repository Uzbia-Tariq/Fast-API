from pathlib import Path
import pickle

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "Mymdoel.pkl"

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)

FEATURES = list(model.feature_names_in_)

app = FastAPI(
    title="Diabetes Prediction API",
    description="A FastAPI service that predicts diabetes using a trained Logistic Regression model.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For this local viva/demo project
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictRequest(BaseModel):
    Glucose: float = Field(..., ge=0, description="Plasma glucose concentration")
    BloodPressure: float = Field(..., ge=0, description="Diastolic blood pressure")
    Insulin: float = Field(..., ge=0, description="2-hour serum insulin")
    BMI: float = Field(..., ge=0, description="Body mass index")
    DiabetesPedigreeFunction: float = Field(..., ge=0, description="Diabetes pedigree function")
    Age: float = Field(..., ge=1, description="Age in years")


@app.get("/")
def home():
    return {
        "message": "Diabetes Prediction API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest):
    input_data = pd.DataFrame([request.model_dump()])[FEATURES]
    predicted_label = int(model.predict(input_data)[0])
    probability = float(model.predict_proba(input_data)[0][1])

    return {
        "predicted_label": predicted_label,
        "prediction": "Diabetic" if predicted_label == 1 else "Not Diabetic",
        "probability": round(probability, 3),
    }
