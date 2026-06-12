FROM python:3.13-slim

LABEL maintainer="LopatoMT@gmail.com"
LABEL org.opencontainers.image.title="ci-cd-edu"
LABEL org.opencontainers.image.description="FastAPI service"
LABEL version="0.1.0"

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root

COPY . .

RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]