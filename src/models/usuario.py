class Usuario:
    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome
    def get_id (self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def set_nome(self, nome: str) -> None:
        self.__nome = nome