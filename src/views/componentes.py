import customtkinter as ctk
from tkinter import messagebox
import base64, io
from datetime import datetime
from PIL import Image, ImageTk

from src.models.tarefa import TarefaAcademica, TarefaPessoal

COR_FUNDO   = "#0d1b3e"
COR_SIDEBAR = "#0a1628"
COR_COLUNA  = "#112244"
COR_CARD    = "#1a2f5e"
COR_BORDA   = "#2a4a8e"
COR_DOURADO = "#f5c842"
COR_ROSA    = "#e8607a"
COR_VERDE   = "#5ecfa0"
COR_TEXTO   = "#f0e8d0"
COR_CINZA   = "#8899bb"

COLUNAS = ["A Fazer", "Em andamento", "Concluído"]

IMAGENS = {
    "principe": "iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAADV0lEQVR4nO2cv08UURDHR2NH7ChEK4trTypzWFiQaCHXamMCxOaq+wf8A6xNqGwMkNhoezSQXGEBhArpjAUVaEFHrLEwz+ytb9++tz++812YT8Pl9ubd7OfmZud27xAxDMMwDMMwDMMwDMPw8/tw+Uo7h1RuaydwU+icaFfNXatqStF1JTK+CJSiRfyy8vfFPIaFO9oJxBCS57bNDaa3cBmlQ5dckxXJJJ8iEcTbXVs6bY++bphoECYahLpo1DimPfapi74pmGgQnfjA8pfVwLZtWBZVIRYdElv2WD7xpK0jRXIb8c1DKLopSVyyVUX/P3I1LWd2Pc0Rj6ii26pAjsomEd22DH3ZBKJREnRlq4oOnbrsjabSG02T1iuL0TxVqnww3PQenHqjqZwdb+242zHExBQ9HwKC1jFLVlis7CoxaOhEi4g8WFxbyf5tKwYJpWiRasJYJYsQiv7xYTnqvroxaOhEi8xKihVWJQaJ6pVhjSlgbrCuss/KczR2p7Uki5C2juuIuuiyKjvdO5LTvaPgGjGP0axmEQLRsRSJLBPMAsVXwkTCB8YYmQ+fPS7cpl3NIkSiRcqnEJ/wkGARDskiZBdnXx4u/fwyOFgo2l4m1bde7aQagqZHv3j//VykOTluHbeuNupvq1/rb6/eLK555Yaqu4iiF+rj8dbCvc13avur8sT98WTibu9e7s+cCHp+98mOL+bg9UXhCaOlT/PemNDaJxvDYWy+TaAqOi/CR5F4HynroUVTHQx9ZOX5pMfIZUBVdF5cmbQqUlPeEW0Cbx3Z/hyiTqXGykW2D9rWkVLtLFUbglZ0nqzM3cv9lS7IzULzgSWFrkkW6ajoLmKiQUBFx04cKJD5WEWDMNEgTDQIEw3CRIOAiWabOByovKyiQZhoECYahIkGYaJBQESzThwORH5W0SAYr7DkL1mlnOSvE9sqbBXtuy4Ye5G2TmzrqH8lLNMfy6SEqjMqFv2lmSzqokVE+uNJ7I+GfLKjqvZkY6i6r4w9uhBXkf3xZJK5TflvjPOw9egoNFtAVTopuouYaBAmGoSJBkE1dVx8/ey9f/7pq1ZjEajP0fcfrSaNZ+fftv/lXCcWjWrrSBWVjakTq4H1aBAmGoSq6Co908XUidXgD0NOO7s+mzqqAAAAAElFTkSuQmCC",
    "planeta":  "iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAADBElEQVR4nO2cvU7cQBRGb9BKKWjzCNSEMkg0gSJF8gaRSESXAgoqGnoqiqSPSLFvQIo0qZCAjqTmEWhJncrSaDRre+b+2vudEmzvneNv7854vSYCAAAAAAAAAAAAAAAAAAAAdbzwLmCI7ePrx7Hb/v32YUuzFg7hRNeIHSKS+BCiJeWuwlu6q2gLwTlewl1EewjOsRa+YfliRDEkE9nXYZboKIJLWKTbJNGRJRPZ1Kee6HwQf76+f7dq29cnP39p19OHZrJVRaeS+wTneArXkq3WOlolt2wviVYbURHNkczdTwIN2eKiJSRL7c9BWrao6Oizi1okx7OQOpAWO0dPF/nfHr6/OvOohYOYaMs0p/K1pW8fXz9KzEREWodny9g5eroopV4SifGprgy58+FPDz/ejt1WWzYXtuihs90qu0Zyh6ZsbqpNrnXUym6R3BE12awleMtZLs2N/90fnHPqGMPu8nRP4jitH4zqom8/Xt5wXsOSMSejVbToPHpKUkuU6pd6JzQn+vlu/0qiACKiLy8PVU5QOseWDMHmm9+fa/epEl0rN0+DxwdV7YKm9oSMlT6qdYwRLPUW86Y0jj75nZsh4StFD8mdi9gx5GMtiU99laQXRZckpzvP7SpdLbvL07109pH7er7bv8plL/IN8oO2NP51o3OU+stbykb+j3RnSK6j5KzzWlyCQzCPkr+meTSnR1tO8TSvVdeuEM1vCVtXzEVbfQ0V7esuJNoIF9HaaYuWZiLHRGvJiCiZyLl1SEuJKpmoUbTkjYBSciwlt4w/xA00naSWOXbkFKeEEN2RSuuTPhW5KaFEp0xRZh/NH4bev9vzonXcWLAYAdFGsESvW/vgjBeJNoItel1SzR0nEm2EiOi5pzrMHf9E85UtNS60DiNERc8t1ZLjEU/0XGRLj0OldUxdtkb9aj16qrIn93QDounJ1qxXfdYxFdnadZpM76LLtqjP/HFske6ttgyA+YIlSrqt68CTHI3As0mNCCE6BU/bdWIuz48GAAAAAACz4j+B110WE4fVLwAAAABJRU5ErkJggg==",
    "raposa":   "iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAD/ElEQVR4nO2cr28UQRTHXwkCg2xFK3oKRznTQKoQJCRA/wFCwCIqqjlH0uoKBBZC+Af6I2mCQJESzAEOdRWtoBJTdxiGDMPM7Jvdmfe+ezcf03b3Znb2k7dvZmfmSlSpVCqVSqVSqVQqlUoxJqPhVLsNKZRs75VSFRv6Irsv7QwyGQ2n6Dch0cbiEW1AlS3VLjHRRHiyJdsjKpoIR7Z0O4qLHuyMF9xj2rJ91/e1MyfiEW3Qkq11XTXRRPI3rfkkqYomkrt57XQlIrop/5WW0FR/6fxMBBDRhlKytSPZACOaKL8UFMlEYKKJ8slBkkwkKDolD3aVlFJeIj8TAUa0oa1stEg2XNVuQIzJaDgd7IwXOPK4n9MCNqINXHnIkomERUvlQy6S7YGP6FkBLkdvHKz9/f3To2/i5UsBFdEbB2t0Nn5zaP8tWb4k4qJDedGW1EZWannp/gIqoleGzx7aP6XLlwRKNFF3SYiSieqaoRgwER0aIXBHDl3LlwZqu4ErJVVSannJqIYbR3eNQJQIdoFJHbOOekRfO3tw3/x+uXJ0HPvs5PTnf8cGq0vZ6i+J6KDdzom2ABefEJ9kg082t/65n/i3iUnmnEdARXQs2tzzi5vbnzl12p9LqV8K0RydsgrCFewr8+v1D3Z7Uq/Rll6kjvWt3aj0pvMIqMzeNfX+15/feOkeC8n0HfeVt7lcOTqWnr1TH96l0IfIDaG2hmdytTvObZObQ1zs7932jaM11i5VF0t9HWNu0e4xrQVi1c7Qd9M+OW1AkkwEkKPNzZecSUPY5gAzvLNldI1quzyCZCLlHB3Cju6UnI0o2ADVGBs3lcSEu08AmmQigBzNJVcnqQVMjp51qmghquiOTEbDE87n4HJ0jvG0qaNkp8gVbIDpnfvwwhKTO9gZ34mVVY9oib0VXSM8NXp9qIrW+C44V3YOuTbq06RcFje3D0PnLvb3kjY2xmR3ERxLHyqiUyTHBLukCLdl54peKNEJi7NswS4JwrOu2MREQ46ju0jOUb4tsScDajcpUT5JzHrE5k8gI7rPhKIaSnTuR14rhfiAEj3LVNEF8KWPuf4uOGUe3sWAG0fnzKuM8XQW0U0TSkRAb4buHuf1rd3Wwr+8evGPYN9G9T87W5PfCDlSfUDMdYQ2kreR7Uo22LK5r99tpfpQ3xLWtFs/RXZIsmGwuhT6X6knOaX6UBX98ckya96DI7tJsuHuu/P523vHpalTS50m1UB9hYVLH2TG6EVEzwK9iGjOiw4332uhLvrx93vBc+9vflCvLxdqo47lW0/ZEXj+9W1jO3PXlxvxC6YIcfEJyl1fKWpnKEQVLUTN0UKozw/HBLURkru+Ss/4Da/CChrvkQYMAAAAAElFTkSuQmCC",
}


def carregar_imagem(nome, tamanho):
    dados = base64.b64decode(IMAGENS[nome])
    imagem = Image.open(io.BytesIO(dados)).resize(tamanho, Image.LANCZOS)
    return ImageTk.PhotoImage(imagem)


def status_para_coluna(status: str) -> str:
    s = status.lower().strip()
    if "andamento" in s:
        return "Em andamento"
    elif s == "concluído" or s == "concluido":
        return "Concluído"
    return "A Fazer"


def criar_card_tarefa(coluna_widget, tarefa, ao_mover, ao_remover):
    eh_academica = isinstance(tarefa, TarefaAcademica)
    cor = COR_VERDE if eh_academica else COR_ROSA
    tag = "🎓 Acadêmica" if eh_academica else "🌹 Pessoal"

    card = ctk.CTkFrame(coluna_widget, fg_color=COR_CARD, corner_radius=14,
                         border_width=1, border_color=COR_BORDA)
    card.pack(fill="x", padx=8, pady=6)

    topo = ctk.CTkFrame(card, fg_color="transparent")
    topo.pack(fill="x", padx=12, pady=(10, 2))

    ctk.CTkLabel(topo, text=tag, font=("Segoe UI", 10, "bold"), text_color=cor)\
        .pack(side="left")
    ctk.CTkButton(topo, text="✕", width=24, height=24, fg_color="transparent",
                  text_color=COR_CINZA, hover_color="#3a1a1a", corner_radius=6,
                  command=lambda: ao_remover(tarefa)).pack(side="right")

    ctk.CTkLabel(card, text=tarefa.get_titulo(), font=("Georgia", 12, "bold"),
                 text_color=COR_TEXTO, wraplength=180, justify="left", anchor="w")\
        .pack(fill="x", padx=12)

    if eh_academica:
        prazo = tarefa.verificar_prazo()
        cor_prazo = COR_ROSA if "vencido" in prazo.lower() else COR_VERDE
        ctk.CTkLabel(card, text=prazo, font=("Segoe UI", 9), text_color=cor_prazo)\
            .pack(anchor="w", padx=12, pady=(2, 0))

    botoes = ctk.CTkFrame(card, fg_color="transparent")
    botoes.pack(fill="x", padx=12, pady=(6, 10))

    indice = COLUNAS.index(status_para_coluna(tarefa.get_status()))
    if indice > 0:
        ctk.CTkButton(botoes, text="◀", width=32, height=26, fg_color=COR_BORDA,
                      corner_radius=8, command=lambda: ao_mover(tarefa, -1))\
            .pack(side="left", padx=(0, 4))
    if indice < len(COLUNAS) - 1:
        ctk.CTkButton(botoes, text="▶", width=32, height=26, fg_color=COR_DOURADO,
                      text_color=COR_FUNDO, corner_radius=8,
                      command=lambda: ao_mover(tarefa, 1)).pack(side="left")


def criar_coluna(area, nome):
    emojis = {"A Fazer": "🌙", "Em andamento": "⭐", "Concluído": "☀️"}
    coluna = ctk.CTkScrollableFrame(area, fg_color=COR_COLUNA, corner_radius=16,
                                     label_text=f"{emojis[nome]}  {nome}",
                                     label_font=("Georgia", 13, "bold"),
                                     label_fg_color=COR_SIDEBAR,
                                     label_text_color=COR_DOURADO, width=220)
    coluna.pack(side="left", fill="both", expand=True, padx=8)
    return coluna


def atualizar_colunas(widgets_colunas, quadro, filtro, ao_mover, ao_remover):
    for widget in widgets_colunas.values():
        for item in widget.winfo_children():
            item.destroy()

    if filtro == "academica":
        tarefas = quadro.filtrar_por_tipo(TarefaAcademica)
    elif filtro == "pessoal":
        tarefas = quadro.filtrar_por_tipo(TarefaPessoal)
    else:
        tarefas = quadro.listar_tarefas()

    for tarefa in tarefas:
        coluna_nome = status_para_coluna(tarefa.get_status())
        if coluna_nome in widgets_colunas:
            criar_card_tarefa(widgets_colunas[coluna_nome], tarefa, ao_mover, ao_remover)

    for widget in widgets_colunas.values():
        if not widget.winfo_children():
            ctk.CTkLabel(widget, text="vazio por enquanto", text_color=COR_CINZA,
                         font=("Georgia", 11, "italic")).pack(pady=24)


def abrir_popup_nova_tarefa(janela, quadro, ao_adicionar):
    popup = ctk.CTkToplevel(janela)
    popup.title("Nova Tarefa")
    popup.geometry("380x440")
    popup.configure(fg_color=COR_SIDEBAR)
    popup.grab_set()

    ctk.CTkLabel(popup, text="🌟 Nova missão", font=("Georgia", 14, "bold"),
                 text_color=COR_DOURADO).pack(pady=(24, 12))

    campo_titulo = ctk.CTkEntry(popup, width=310, height=40, corner_radius=12,
                                 placeholder_text="título",
                                 fg_color=COR_CARD, border_color=COR_BORDA,
                                 text_color=COR_TEXTO, placeholder_text_color=COR_CINZA)
    campo_titulo.pack(pady=4)

    campo_descricao = ctk.CTkEntry(popup, width=310, height=40, corner_radius=12,
                                    placeholder_text="descrição",
                                    fg_color=COR_CARD, border_color=COR_BORDA,
                                    text_color=COR_TEXTO, placeholder_text_color=COR_CINZA)
    campo_descricao.pack(pady=4)

    tipo_var = ctk.StringVar(value="pessoal")
    menu_tipo = ctk.CTkOptionMenu(popup, values=["pessoal", "academica"], variable=tipo_var,
                                   width=310, height=38, fg_color=COR_CARD,
                                   button_color=COR_DOURADO, text_color=COR_TEXTO)
    menu_tipo.pack(pady=4)

    frame_acad = ctk.CTkFrame(popup, fg_color="transparent")
    campo_disciplina = ctk.CTkEntry(frame_acad, width=310, height=38, corner_radius=12,
                                     placeholder_text="disciplina",
                                     fg_color=COR_CARD, border_color=COR_BORDA,
                                     text_color=COR_TEXTO, placeholder_text_color=COR_CINZA)
    campo_disciplina.pack(pady=3)
    campo_data = ctk.CTkEntry(frame_acad, width=310, height=38, corner_radius=12,
                               placeholder_text="data de entrega (dd/mm/aaaa)",
                               fg_color=COR_CARD, border_color=COR_BORDA,
                               text_color=COR_TEXTO, placeholder_text_color=COR_CINZA)
    campo_data.pack(pady=3)
    campo_prioridade = ctk.CTkEntry(frame_acad, width=310, height=38, corner_radius=12,
                                     placeholder_text="prioridade (alta/média/baixa)",
                                     fg_color=COR_CARD, border_color=COR_BORDA,
                                     text_color=COR_TEXTO, placeholder_text_color=COR_CINZA)
    campo_prioridade.pack(pady=3)

    def ao_mudar_tipo(valor):
        frame_acad.pack(pady=4) if valor == "academica" else frame_acad.pack_forget()

    menu_tipo.configure(command=ao_mudar_tipo)

    def salvar():
        titulo = campo_titulo.get().strip()
        descricao = campo_descricao.get().strip() or "-"
        if not titulo:
            return
        if tipo_var.get() == "academica":
            try:
                data = datetime.strptime(campo_data.get().strip(), "%d/%m/%Y").date()
            except ValueError:
                messagebox.showerror("Erro", "Data inválida! Use dd/mm/aaaa")
                return
            tarefa = TarefaAcademica(titulo, descricao, "a concluir",
                                      campo_disciplina.get().strip() or "-",
                                      data, campo_prioridade.get().strip() or "média")
        else:
            tarefa = TarefaPessoal(titulo, descricao, "a concluir")

        quadro.adicionar_tarefa(tarefa)
        ao_adicionar()
        popup.destroy()

    ctk.CTkButton(popup, text="Adicionar", width=310, height=44, fg_color=COR_DOURADO,
                  text_color=COR_FUNDO, font=("Segoe UI", 12, "bold"),
                  corner_radius=12, command=salvar).pack(pady=16)