from fastapi import FastAPI
from typing import Optional
import pandas as pd
import json
from data_request_model import *
import joblib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()

# Загрузка модели AdaBoost
ada_model = joblib.load('ada_model.pkl')
# Загрузка модели Random Forest
random_forest_model = joblib.load('random_forest_model.pkl')
# Загрузка модели Logistic Regression
logistic_regression_model = joblib.load('baseline_model.pkl')


def predict_logistic_regression_model(IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA):
    prediction = logistic_regression_model.predict(
        pd.DataFrame([[IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA]],
                     columns=['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']))
    return prediction

def predict_random_forest_model(IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA):
    prediction = random_forest_model.predict(
        pd.DataFrame([[IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA]],
                     columns=['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']))
    return prediction

def predict_ada_model(IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA):
    prediction = ada_model.predict(
        pd.DataFrame([[IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA]],
                     columns=['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']))
    return prediction

@app.post("/model-predict")
async def ml_predict(inputs: dict):
    selected_model = inputs['model']
    selected_values = inputs['parameters']

    if selected_model == 'AdaBoost':
        prediction = predict_ada_model(**selected_values)
    elif selected_model == 'Random Forest':
        prediction = predict_random_forest_model(**selected_values)
    elif selected_model == 'Logistic Regression':
        prediction = predict_logistic_regression_model(**selected_values)

    return prediction[0]
