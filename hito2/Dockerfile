FROM python:3.12-slim
RUN useradd --create-home --uid 10001 appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
USER appuser
CMD ["gunicorn", "--workers", "2" ,"--bind", "0.0.0.0:5000", "app:app"]