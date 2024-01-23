# ./backend/Dockerfile
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install fastapi[all] uvicorn pillow pandas numpy joblib scikit-learn==1.2.2
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]