FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

ENV SERPER_API_KEY="INSERT_UR_OWN_API_KEY_HERE_PLZ"

CMD ["python", "server.py"]

