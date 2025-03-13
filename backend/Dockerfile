FROM python:3.12-slim

WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m -r -s /bin/bash myuser
RUN chown -R myuser:myuser /app
USER myuser

EXPOSE 5000

CMD ["python", "app.py"]