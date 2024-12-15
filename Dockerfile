FROM python:3.11

WORKDIR /app

COPY prod_requirements.txt /app/tmp/requirements.txt

RUN pip install --no-cache-dir -r /app/tmp/requirements.txt

COPY app.py .
COPY ./model/model.joblib /app/model/model.joblib

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
