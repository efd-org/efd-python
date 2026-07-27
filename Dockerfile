FROM python:3.10-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /src

# Copy dependency list early to leverage build cache
COPY requirements.txt .

# Install build tools for any packages that need compilation, create a venv and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && if [ -s requirements.txt ]; then /opt/venv/bin/pip install --no-cache-dir -r requirements.txt; fi \
    && rm -rf /var/lib/apt/lists/* /root/.cache

# Copy application source
COPY app.py .

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH

# Create a non-root user for running the app
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

# Copy venv and application from the builder stage
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /src/app.py ./app.py

# Ensure files are owned by the non-root user
RUN chown -R appuser:appuser /opt/venv /app

USER appuser

EXPOSE 8080

ENTRYPOINT ["/opt/venv/bin/python", "/app/app.py"]