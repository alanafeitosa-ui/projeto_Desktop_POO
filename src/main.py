from src.views.menu import Menu
from src.database.conexao import criar_tabelas

if __name__ == "__main__":
    criar_tabelas()
    Menu()