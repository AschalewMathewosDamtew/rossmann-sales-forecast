from fastapi import APIRouter
from app.models.model import predict

router = APIRouter()

@router.post("/predict")
def get_prediction(feature_1: float, feature_2: float):
    prediction = predict(feature_1, feature_2)
    return {"prediction": prediction}
