FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
