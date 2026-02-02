FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y chromium chromium-driver curl && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/app
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

COPY app/ app/
COPY tests/ tests/
COPY pytest.ini .
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    pytest pytest-html pytest-cov selenium requests

CMD ["pytest"]
