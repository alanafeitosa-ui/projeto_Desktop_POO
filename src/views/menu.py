from src.models.tarefa import TarefaAcademica, TarefaPessoal
from src.models.quadro import Quadro
from datetime import datetime

class Menu:
    def __init__(self):
        self.__quadro = None
        self.executar()
    def executar(self):
        while True:
            print("\n===== MENU GERENCIAMENTO =====")
            print("1 - Criar quadro")
            print("2 - Criar tarefa academica")
            print("3 - Criar tarefa Pessoal")
            print("4 - Filtrar tarefas")
            print("5 - Remover tarefa")
            print("6 - Alterar status para em andamento")
            print("7 - Alterar status para concluida")
            print("8 - Listar tarefas")
            print("9 - Exibir detalhes das tarefas")
            print("10 - Parar programa")
            opcao = str(input("Insira a seguir uma das opções acima: "))

            match opcao:
                case "1":
                    nome_quadro = str(input("Insira a seguir o nome desejado do quadro: "))
                    self.__quadro = Quadro(nome_quadro)

                case "2":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!\n")
                    else:
                        quantia_tarefa_academica = int(input("Insira a seguir a quantidade de tarefas acadêmicas que deseja criar: "))
                        tarefas_academicas = []
                        for i in range(quantia_tarefa_academica):
                            print(f"\n=== Cadastro tarefa acadêmica {i + 1} ===")
                            titulo = str(input(f"Insira a seguir o titulo da tarefa: "))
                            descricao = str(input("Insira a seguir uma breve descrição sobre a tarefa: "))
                            status = str(input("A tarefa está: a concluir, em andamento ou concluída? "))
                            disciplina = str(input("Insira a seguir a disciplina referente a tarefa: "))
                            data_entrega = str(input("Insira a data de entrega da tarefa no formato (dd/mm/aaaa): "))
                            data_convertida = datetime.strptime(data_entrega, "%d/%m/%Y").date()
                            prioridade = str(input("Insira a seguir a ordem de prioridade da tarefa: \n"))
                            
                            tarefa_acad = TarefaAcademica(titulo, descricao, status, disciplina, data_convertida, prioridade)
                            tarefas_academicas.append(tarefa_acad)
                        for tarefa in tarefas_academicas:
                            self.__quadro.adicionar_tarefa(tarefa)

                case "3":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!\n")
                    else:
                        quantia_tarefa_pessoal = int(input("Insira a seguir a quantidade de tarefas pessoais que deseja criar: \n"))
                        tarefas_pessoais = []
                        for i in range(quantia_tarefa_pessoal):
                            print(f"\n=== Cadastro tarefa pessoal {i + 1} ===")
                            titulo = str(input("Insira a seguir o titulo da tarefa: "))
                            descricao = str(input("Insira a seguir uma breve descrição sobre a tarefa: "))
                            status = str(input("A tarefa está: a concluir, em andamento ou concluída?\n"))
                            tarefa_pes = TarefaPessoal(titulo, descricao, status)
                            tarefas_pessoais.append(tarefa_pes)
                        for tarefa in tarefas_pessoais:
                            self.__quadro.adicionar_tarefa(tarefa)

                case "4":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!\n")
                    else:
                        tipo = input("Deseja filtrar as tarefas pelo tipo tarefa academica ou tarefa pessoal? ").lower().strip()
                        if tipo == "tarefa academica":
                            tarefas = self.__quadro.filtrar_por_tipo(TarefaAcademica)
                        elif tipo == "tarefa pessoal":
                            tarefas = self.__quadro.filtrar_por_tipo(TarefaPessoal)
                        else:
                            print("entrada invalida, por favor digite uma das duas opções apresentadas")
                            continue
                        for tarefa in tarefas:
                            print(f"{tarefa}\n")

                case "5":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!")
                    else:
                        pass

                case "6": 
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!")
                    else:
                        pass

                case "7":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!")
                    else:
                        pass

                case "8":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!")
                    else:
                        for i, tarefa in enumerate(self.__quadro.listar_tarefas(), start=1):
                            print(f"{i}. {tarefa}\n")

                case "9":
                    if self.__quadro is None:
                        print("Necessário criar um quadro antes de realizar esta ação!")
                    else:
                        for i in self.__quadro.listar_tarefas():
                            print (f"{i.exibir_detalhes()}\n")

                case "10":
                    print("Encerrado sistema...")
                    break

                case _:
                    print("Opção inválida!\n")