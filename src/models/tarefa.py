from abc import ABC, abstractmethod

class Tarefa(ABC):
    def __init__(self, titulo: str, descricao: str, status: str):
       self.__titulo = titulo
       self.__descricao = descricao
       self.__status = status
    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass
    def mover_para_andamento(self) -> None:
        self.__status = "Em andamento"
    def mover_para_concluido(self) -> None:
        self.__status = "Concluído"
    def get_titulo(self) -> str:
        return self.__titulo
    def set_titulo (self, titulo: str) -> None:
        self.__titulo = titulo
    def get_descricao(self) -> str:
        return self.__descricao
    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao
    def get_status(self) -> str:
        return self.__status
    def set_status(self, status: str) -> None:
        self.__status = status

class TarefaPessoal(Tarefa):
    def __init__(self, titulo:str, descricao: str, status: str):
        super().__init__(titulo, descricao, status)
    def exibir_detalhes(self) -> str:
        return (f"Titulo: {self.get_titulo()};\n Descriçao: {self.get_descricao()};\n"
                f"Status: {self.get_status()}")
    
class TarefaAcademica(Tarefa):
    def __init__(self, titulo: str, descricao: str, status: str, disciplina: str, data_entrega: str, prioridade: str):
        super().__init__(titulo, descricao, status)
        self.__disciplina = disciplina
        self.__data_entrega = data_entrega
        self.__prioridade = prioridade
    def get_disciplina(self) -> str:
        return self.__disciplina
    def set_disciplina(self, disciplina: str) -> None:
        self.__disciplina = disciplina
    def get_data_entrega(self) -> str:
        return self.__data_entrega
    def set_data_entrega(self, data_entrega: str) -> None:
        self.__data_entrega = data_entrega
    def get_prioridade(self) -> str:
        return self.__prioridade
    def set_prioridade(self, prioridade:str) -> None:
        self.__prioridade = prioridade
    def exibir_detalhes(self) -> str:
        return (f"Titulo: {self.get_titulo()};\n Descriçao: {self.get_descricao()};\n"
                f"Status: {self.get_status()};\n Disciplina: {self.get_disciplina()};\n"
                f"Data de entrega: {self.get_data_entrega()};\n Prioridade: {self.get_prioridade()}")
    def verificar_prazo(self) -> str:
        return self.get_data_entrega()