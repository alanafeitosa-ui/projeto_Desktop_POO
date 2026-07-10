import sqlite3
DATABASE = "kaban.db"
def conectar():
    return sqlite3.connect(DATABASE)
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS quadro(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL
                   )
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tarefa(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   descricao TEXT,
                   status TEXT NOT NULL,
                   tipo TEXT NOT NULL,
                   disciplina TEXT,
                   data_entrega TEXT,
                   prioridade TEXT, 
                   quadro_id INTEGER,
                   FOREIGN KEY (quadro_id) REFERENCES quadro(id) ON DELETE CASCADE
                   )
                   """)
    conn.commit()
    conn.close()