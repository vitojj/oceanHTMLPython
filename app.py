import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "kiara"

app = Flask(__name__)
app.config.from_object(obj(__name__))

def conectardb():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.db = conectardb()

@app.teardown_request
def pos_requisicao(exception):
    g.db.close()


@app.route('/')
def index():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cursor = g.db.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return str(entradas)
