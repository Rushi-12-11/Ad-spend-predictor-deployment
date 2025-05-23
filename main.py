from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()  # <-- create app instance before routes

model = joblib.load("saved_models/03.randomforest_with_advertising.pkl")

@app.get("/")
async def root():
    return {"message": "API is up and running"}
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as f:
        return f.read()

class Advertising(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

@app.post("/prediction/advertising")
def predict_advertising(request: Advertising):
    features = [[request.TV, request.Radio, request.Newspaper]]
    prediction = model.predict(features)
    return {"prediction": prediction[0]}
