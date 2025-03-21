# Pull base image
FROM python:3.10-slim

# Set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working dir
WORKDIR /code

# Install dependencies
COPY ./pyproject.toml .
COPY ./uv.lock .

RUN pip install uv

RUN uv pip install -r pyproject.toml --system

# Copy core
COPY . /code/
