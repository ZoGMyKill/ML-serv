import streamlit as st
import requests
import pandas as pd
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Функция для аутентификации пользователя
def authenticate(username, password):
    return username == "admin" and password == "admin"


# Функция для регистрации нового пользователя
def register(username, password):
    # Здесь можно добавить логику для сохранения нового пользователя
    st.success("Регистрация успешно завершена!")

def main():
    # Инициализация состояния сеанса
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    authentication_page()

    # Показываем основной интерфейс, только если аутентификация выполнена
    if st.session_state['authenticated']:
        show_main_interface()

def authentication_page():
    st.set_page_config(layout='wide')

    st.title("Добро пожаловать на наш сервис!\n\nЗарегистрируйтесь или войдите в свой аккаунт!")

    # Создаем сайдбар
    st.sidebar.title("Меню")

    # Выбор действия: Аутентификация или Регистрация
    action = st.sidebar.radio("Выберите действие:", ("Аутентификация", "Регистрация"))

    if action == "Аутентификация":
        st.sidebar.header("Аутентификация")

        # Поля для ввода имени пользователя и пароля
        username = st.sidebar.text_input("Имя пользователя")
        password = st.sidebar.text_input("Пароль", type="password")

        # Кнопка для входа
        if st.sidebar.button("Войти"):
            if authenticate(username, password):
                st.success("Вход выполнен успешно!")
                st.sidebar.success("Вход выполнен успешно!")
                st.session_state['authenticated'] = True  # Обновляем состояние аутентификации

    elif action == "Регистрация":
        st.sidebar.header("Регистрация")

        # Поля для ввода имени пользователя и пароля для регистрации
        new_username = st.sidebar.text_input("Новое имя пользователя")
        new_password = st.sidebar.text_input("Новый пароль", type="password")

        # Кнопка для регистрации
        if st.sidebar.button("Зарегистрироваться"):
            register(new_username, new_password)


# Функция для отображения основного интерфейса
def show_main_interface():
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
    selected_model = st.selectbox('Выберите модель для предсказания:',
                                  ['AdaBoost', 'Random Forest', 'Logistic Regression'])

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


if __name__ == "__main__":
    main()
