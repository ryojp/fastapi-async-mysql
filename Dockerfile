FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root
COPY ./ ./
CMD ["python", "fastapi_async_mysql/main.py"]
