# ./frontend/Dockerfile
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install streamlit requests pillow
CMD ["streamlit", "run", "ml_app_with_fastapi.py", "--server.address=0.0.0.0"]