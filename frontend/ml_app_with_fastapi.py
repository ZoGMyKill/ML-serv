import streamlit as st
import pandas as pd
import requests
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# Set Page Layout
st.set_page_config(layout='wide')

st.title('Классификация глиомы мозга')
st.image("""https://medtour.help/wp-content/uploads/2023/08/glioma-priznaki-1.jpg""")
st.header('Ввод 20 молекулярных признаков:')

# Создаем список параметров
parameters = ['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1',
              'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']

# Создаем словарь для хранения выбранных значений
user_inputs = {}

# Добавим интерфейс для выбора значений для каждого параметра
for parameter in parameters:
    choice = st.radio(f'Выберите значение для {parameter}:', ['NOT_MUTATED', 'MUTATED'])
    user_input = 0 if choice == 'NOT_MUTATED' else 1
    user_inputs[parameter] = user_input

# Добавим интерфейс для выбора модели
selected_model = st.selectbox('Выберите модель для предсказания:', ['AdaBoost', 'Random Forest', 'Logistic Regression'])

if st.button('Предсказать диагноз'):
    inputs = {
        'parameters': user_inputs,
        'model': selected_model
    }
    response = requests.post("http://backend:8000/model-predict", json=inputs)

    if response.status_code == 200:
        st.success(f'Предсказанный диагноз: {response.text}')
    else:
        st.error('Ошибка предсказания')
