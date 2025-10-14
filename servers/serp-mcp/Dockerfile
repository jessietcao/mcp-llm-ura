FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

ENV SERPER_API_KEY=21825f410c17b13f5c8cb5cff94479ab12801a67

CMD ["python", "server.py"]

