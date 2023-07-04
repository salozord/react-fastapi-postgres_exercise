FROM python:3.9-slim as builder

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt


FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/t/lists/*

COPY --from=builder /opt/venv /opt/venv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /back

COPY . /back
