import customtkinter as ctk

from src.models.quadro import Quadro
from src.views.componentes import (
    carregar_imagem, criar_coluna, atualizar_colunas,
    abrir_popup_nova_tarefa, status_para_coluna, COLUNAS,
    COR_FUNDO, COR_SIDEBAR, COR_DOURADO, COR_CINZA,
    COR_CARD, COR_BORDA, COR_TEXTO
)


def criar_tela_principal(janela, quadro):
    estado = {"filtro": "todas"}

    tela = ctk.CTkFrame(janela, fg_color=COR_FUNDO)
    tela.place(relx=0, rely=0, relwidth=1, relheight=1)

    sidebar = ctk.CTkFrame(tela, fg_color=COR_SIDEBAR, width=210, corner_radius=0)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    ctk.CTkLabel(sidebar, text="🌹", font=("Segoe UI", 64)).pack(pady=(28, 0))

    ctk.CTkLabel(sidebar, text="Pequeno Príncipe", font=("Georgia", 13, "bold"),
                 text_color=COR_DOURADO).pack(pady=(8, 0))
    ctk.CTkLabel(sidebar, text="seu asteroide particular", font=("Georgia", 9, "italic"),
                 text_color=COR_CINZA).pack(pady=(2, 14))

    ctk.CTkFrame(sidebar, height=1, fg_color=COR_BORDA).pack(fill="x", padx=16, pady=4)
    ctk.CTkLabel(sidebar, text="✦ FILTRAR", font=("Segoe UI", 9, "bold"),
                 text_color=COR_CINZA).pack(anchor="w", padx=16, pady=(8, 4))

    def mudar_filtro(valor):
        estado["filtro"] = valor
        atualizar_colunas(widgets_colunas, quadro, estado["filtro"], mover_tarefa, remover_tarefa)

    for texto, valor in [("🌟 Todas", "todas"), ("🎓 Acadêmicas", "academica"), ("🌹 Pessoais", "pessoal")]:
        ctk.CTkButton(sidebar, text=texto, anchor="w", fg_color="transparent",
                      hover_color="#1a2f5e", text_color=COR_TEXTO, corner_radius=10,
                      command=lambda v=valor: mudar_filtro(v)).pack(fill="x", padx=10, pady=2)

    ctk.CTkLabel(sidebar, text="🌍  🦊  ⭐", font=("Segoe UI", 22),
                 text_color="#fffacd").pack(side="bottom", pady=(0, 12))
    ctk.CTkLabel(sidebar, text="✦ ✧ ⋆ ✦ ✧ ⋆", font=("Segoe UI", 10),
                 text_color="#fffacd").pack(side="bottom", pady=4)

    area = ctk.CTkFrame(tela, fg_color=COR_FUNDO)
    area.pack(side="left", fill="both", expand=True)

    cabecalho = ctk.CTkFrame(area, fg_color=COR_SIDEBAR, height=64, corner_radius=0)
    cabecalho.pack(fill="x")
    cabecalho.pack_propagate(False)

    ctk.CTkLabel(cabecalho, text="✦  Meu Asteroide de Tarefas  ✦",
                 font=("Georgia", 17, "bold"), text_color="#fffacd")\
        .pack(side="left", padx=24, pady=18)

    def mover_tarefa(tarefa, direcao):
        indice = COLUNAS.index(status_para_coluna(tarefa.get_status()))
        novo = indice + direcao
        if novo == 1:
            tarefa.mover_para_andamento()
        elif novo == 2:
            tarefa.mover_para_concluido()
        else:
            tarefa.set_status("a concluir")
        atualizar_colunas(widgets_colunas, quadro, estado["filtro"], mover_tarefa, remover_tarefa)

    def remover_tarefa(tarefa):
        quadro.remover_tarefa(tarefa)
        atualizar_colunas(widgets_colunas, quadro, estado["filtro"], mover_tarefa, remover_tarefa)

    def nova_tarefa():
        abrir_popup_nova_tarefa(
            janela, quadro,
            lambda: atualizar_colunas(widgets_colunas, quadro, estado["filtro"], mover_tarefa, remover_tarefa)
        )

    ctk.CTkButton(cabecalho, text="🌹 Nova Tarefa", height=38, fg_color=COR_DOURADO,
                  text_color=COR_FUNDO, font=("Segoe UI", 12, "bold"),
                  corner_radius=12, command=nova_tarefa).pack(side="right", padx=24, pady=12)

    area_colunas = ctk.CTkFrame(area, fg_color=COR_FUNDO)
    area_colunas.pack(fill="both", expand=True, padx=16, pady=16)

    widgets_colunas = {}
    for nome in COLUNAS:
        widgets_colunas[nome] = criar_coluna(area_colunas, nome)

    atualizar_colunas(widgets_colunas, quadro, estado["filtro"], mover_tarefa, remover_tarefa)


def iniciar():
    janela = ctk.CTk()
    janela.title("O Pequeno Príncipe — Kanban")
    janela.geometry("1100x680")
    janela.configure(fg_color=COR_FUNDO)
    criar_tela_principal(janela, Quadro("Meu Quadro"))
    janela.mainloop()