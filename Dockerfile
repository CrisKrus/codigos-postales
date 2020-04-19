FROM python:3.6.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./*.py .

CMD python ./main.py
