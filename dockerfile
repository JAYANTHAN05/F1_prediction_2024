FROM python:3.10

COPY . /f1_prediction
WORKDIR /f1_prediction

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "f1_prediction_2024.py"]