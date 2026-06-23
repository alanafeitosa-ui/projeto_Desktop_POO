from src.models.tarefa import tarefaAcademica, tarefaPessoal
class Quadro:
    def __init__(self, titulo, filtro):
        self.__tarefas = []
        self.__titulo = titulo
        self.__filtro = filtro
    def get_tarefas(self):
        return self.__tarefas
    def set_tarefas(self, tarefa):
        self.__tarefas = tarefa
    def adicionar_tarefa(self, tarefa):
        self.get_tarefas().append(tarefa)
    def remover_tarefa(self, tarefa):
        self.get_tarefas().remove(tarefa)
    def listar_tarefas(self):
        return self.get_tarefas()
    def filtrarPorTipo (self, tipo):
        tarefas_filtradas = []
        for p in self.__tarefas:
            if isinstance (p, tipo):
                tarefas_filtradas.append(p)
        return tarefas_filtradas