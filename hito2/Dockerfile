# Lo que necesito para CONSTRUIR mi app
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Lo que necesito para EJECUTAR mi app
FROM python:3.12-slim
RUN useradd --create-home --uid 10001 appuser
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . .
USER appuser
CMD ["gunicorn","--workers","2","--bind","0.0.0.0:5000","app:app"]