FROM python:3.14.4-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["python3", "app.py"]

HEALTHCHECK --interval=60s --timeout=10s --retries=3 CMD curl --fail http://localhost:8080/ || exit 1