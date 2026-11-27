import os
import psycopg
from flask import Flask, jsonify, request

app = Flask(__name__)

# Los datos de conexión vienen de VARIABLES DE ENTORNO (-e), no van escritos en el código
def conectar():
    return psycopg.connect(
        host=os.environ["DB_HOST"],          # el NOMBRE del contenedor de la base
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

def crear_tabla(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS notas (id SERIAL PRIMARY KEY, texto VARCHAR(100))")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/notas")                           # ver todas las notas
def listar():
    with conectar() as conn:
        crear_tabla(conn)
        filas = conn.execute("SELECT id, texto FROM notas ORDER BY id").fetchall()
    return jsonify([{"id": f[0], "texto": f[1]} for f in filas])

@app.post("/notas")                          # guardar una nota nueva
def guardar():
    texto = request.json["texto"]
    with conectar() as conn:
        crear_tabla(conn)
        conn.execute("INSERT INTO notas (texto) VALUES (%s)", (texto,))
    return jsonify(mensaje="nota guardada"), 201