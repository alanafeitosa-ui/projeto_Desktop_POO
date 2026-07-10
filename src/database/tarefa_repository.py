from src.database.conexao import conectar
from src.models.tarefa import TarefaAcademica, TarefaPessoal
def salvar_tarefa(tarefa, quadro_id):
    conn = conectar()
    cursor = conn.cursor()
    if isinstance(tarefa, TarefaAcademica):
        tipo = "academica"
        disciplina = tarefa.get_disciplina()
        data_entrega = tarefa.get_data_entrega().isoformat()
        prioridade = tarefa.get_prioridade()
    else:
        tipo = "pessoal"
        disciplina = None
        data_entrega = None
        prioridade = None
    cursor.execute("""
                   INSERT INTO tarefa(titulo, descricao, status, tipo, disciplina, data_entrega, prioridade, quadro_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   """, (tarefa.get_titulo(), tarefa.get_descricao(), tarefa.get_status(), tipo, disciplina, data_entrega, prioridade, quadro_id))
    tarefa.set_id(cursor.lastrowid)
    conn.commit()
    conn.close()

def listar_tarefas(quadro_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefa WHERE quadro_id = ? ", (quadro_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_status(id, novo_status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefa SET status = ? WHERE id = ?", (novo_status, id))
    conn.commit()
    conn.close()

def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefa WHERE id = ?", (id,))
    conn.commit()
    conn.close()