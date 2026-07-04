from typing import List
from src.models.tarefa import Tarefa
class Quadro:
    def __init__(self, titulo: str):
        self.__tarefas: List[Tarefa] = []
        self.__titulo = titulo
    def get_tarefas(self):
        return self.__tarefas
    def set_tarefas(self, tarefa: Tarefa):
        self.__tarefas = tarefa
    def adicionar_tarefa(self, tarefa: Tarefa):
        self.get_tarefas().append(tarefa)
    def remover_tarefa(self, tarefa: Tarefa):
        self.get_tarefas().remove(tarefa)
    def listar_tarefas(self):
        return self.get_tarefas()
    def filtrar_por_tipo (self, tipo: str):
        tarefas_filtradas = []
        for p in self.__tarefas:
            if isinstance (p, tipo):
                tarefas_filtradas.append(p)
        return tarefas_filtradas