from src.database.conexao import conectar
def salvar_quadro(quadro):
    conn = conectar ()
    cursor = conn.cursor()
    id_gerado = cursor.lastrowid
    cursor.execute("INSERT INTO quadro(titulo) VALUES (?)", (quadro.get_titulo(),))
    conn.commit()
    conn.close()
    return id_gerado

def buscar_quadro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quadro WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def deletar_quadro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quadro WHERE id = ?", (id,))
    conn.commit()
    conn.close()