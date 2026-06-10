from abc import ABC, abstractmethod

class tarefa(ABC):
    def __init__(self, titulo, descricao, status):
       self.__titulo = titulo
       self.__descricao = descricao
       self.__status = status
    @abstractmethod
    def exibirDetalhes(self):
        pass
    def moverParaAndamento(self):
        self.__status = "Em andamento"
    def moverParaConcluido(self):
        self.__status = "Concluido"
    def get_titulo(self):
        return self.__titulo
    def set_titulo (self, titulo):
        self.__titulo = titulo
    def get_descricao(self):
        return self.__descricao
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

class tarefaPessoal(tarefa):
    def __init__(self, titulo, descricao, status):
        super().__init__(titulo, descricao, status)
    def exibirDetalhes(self):
        return (f"Titulo: {self.get_titulo()};\n Descriçao: {self.get_descricao()};\n"
                f"Status: {self.get_status()}")
    
class tarefaAcademica(tarefa):
    def __init__(self, titulo, descricao, status, disciplina, data_entrega, prioridade):
        super().__init__(titulo, descricao, status)
        self.__disciplina = disciplina
        self.__data_entrega = data_entrega
        self.__prioridade = prioridade
    def get_disciplina(self):
        return self.__disciplina
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    def get_data_entrega(self):
        return self.__data_entrega
    def set_data_entrega(self, data_entrega):
        self.__data_entrega = data_entrega
    def get_prioridade(self):
        return self.__prioridade
    def set_prioridade(self, prioridade):
        self.__prioridade = prioridade
    def exibirDetalhes(self):
        return (f"Titulo: {self.get_titulo()};\n Descriçao: {self.get_descricao()};\n"
                f"Status: {self.get_status()};\n Disciplina: {self.get_disciplina()};\n"
                f"Data de entrega: {self.get_data_entrega()};\n Prioridade: {self.get_prioridade()}")
    def verificarPrazo(self):
        return self.get_data_entrega()