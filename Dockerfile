FROM python:3.9.4-slim

ENV PYTHONPATH=/app

WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ ./

CMD [ "python3", "main.py" ]
