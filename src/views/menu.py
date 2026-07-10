from src.models.tarefa import TarefaAcademica, TarefaPessoal
from src.models.quadro import Quadro
from datetime import datetime
from src.database.quadro_repository import salvar_quadro, buscar_quadro, deletar_quadro
from src.database.tarefa_repository import salvar_tarefa, listar_tarefas, atualizar_status, deletar_tarefa

class Menu:
    def __init__(self):
        self._quadro = None
        self._quadro_id = None
        self._carregar_quadro()
        self.executar()
    def __verificar_quadro (self) -> bool :
        if self._quadro is None:
            print("\nNecessário criar um quadro antes de realizar esta ação!\n")
            return False
        return True
    def _carregar_quadro(self):
        from src.database.quadro_repository import buscar_quadro
        resultado = buscar_quadro(1)
        if resultado:
            self._quadro_id = resultado[0]
            self._quadro = Quadro(resultado[1])
            self._carregar_tarefas()
    def _carregar_tarefas(self):
        from src.database.tarefa_repository import listar_tarefas
        from datetime import date
        tarefas = listar_tarefas(self._quadro_id)
        for t in tarefas:
            id, titulo, descricao, status, tipo, disciplina, data_entrega, prioridade, quadro_id = t
            if tipo == "academica":
                data = date.fromisoformat(data_entrega)
                tarefa = TarefaAcademica(titulo, descricao, status, disciplina, data, prioridade)
            else:
                tarefa = TarefaPessoal(titulo, descricao, status)
            tarefa.set_id(id)
            self._quadro.adicionar_tarefa(tarefa)
    def executar(self):
        while True:
            print("\n===== MENU GERENCIAMENTO =====")
            print("1 - Criar quadro")
            print("2 - Criar tarefa acadêmica")
            print("3 - Criar tarefa Pessoal")
            print("4 - Filtrar tarefas")
            print("5 - Remover tarefa")
            print("6 - Alterar status para em andamento")
            print("7 - Alterar status para concluído")
            print("8 - Listar tarefas")
            print("9 - Exibir detalhes das tarefas")
            print("10 - verificar prazo de alguma tarefa acadêmica")
            print("11 - Parar programa")
            opcao = str(input("Insira a seguir uma das opções acima: ").strip())

            match opcao:
                case "1":
                    nome_quadro = str(input("Insira a seguir o nome desejado do quadro: ").strip())
                    self._quadro = Quadro(nome_quadro)
                    self._quadro_id = salvar_quadro(self._quadro)

                case "2":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        quantia_tarefa_academica = int(input("Insira a seguir a quantidade de tarefas acadêmicas que deseja criar: ").strip())
                        tarefas_academicas = []
                        for i in range(quantia_tarefa_academica):
                            print(f"\n=== Cadastro tarefa acadêmica {i + 1} ===")
                            titulo = str(input(f"Insira a seguir o titulo da tarefa: ").strip())
                            descricao = str(input("Insira a seguir uma breve descrição sobre a tarefa: ").strip())
                            status = str(input("A tarefa está: a concluir, em andamento ou concluída? ").strip())
                            disciplina = str(input("Insira a seguir a disciplina referente a tarefa: ").strip())
                            data_entrega = str(input("Insira a data de entrega da tarefa no formato (dd/mm/aaaa): ").strip())
                            data_convertida = datetime.strptime(data_entrega, "%d/%m/%Y").date()
                            prioridade = str(input("Insira a seguir o nível de prioridade da tarefa: ").strip())
                            
                            tarefa_acad = TarefaAcademica(titulo, descricao, status, disciplina, data_convertida, prioridade)
                            tarefas_academicas.append(tarefa_acad)
                        for tarefa in tarefas_academicas:
                            self._quadro.adicionar_tarefa(tarefa)
                            salvar_tarefa(tarefa_acad, self._quadro_id)

                case "3":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        quantia_tarefa_pessoal = int(input("\nInsira a seguir a quantidade de tarefas pessoais que deseja criar: ").strip())
                        tarefas_pessoais = []
                        for i in range(quantia_tarefa_pessoal):
                            print(f"\n=== Cadastro tarefa pessoal {i + 1} ===")
                            titulo = str(input("Insira a seguir o titulo da tarefa: ").strip())
                            descricao = str(input("Insira a seguir uma breve descrição sobre a tarefa: ").strip())
                            status = str(input("A tarefa está: a concluir, em andamento ou concluída? ").strip())
                            tarefa_pes = TarefaPessoal(titulo, descricao, status)
                            tarefas_pessoais.append(tarefa_pes)
                        for tarefa in tarefas_pessoais:
                            self._quadro.adicionar_tarefa(tarefa)
                            salvar_tarefa(tarefa, self._quadro_id)

                case "4":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        tipo = input("Deseja filtrar as tarefas pelo tipo tarefa acadêmica ou tarefa pessoal? ").lower().strip()
                        if tipo == "tarefa academica" or tipo == "tarefa acadêmica":
                            tarefas = self._quadro.filtrar_por_tipo(TarefaAcademica)
                        elif tipo == "tarefa pessoal":
                            tarefas = self._quadro.filtrar_por_tipo(TarefaPessoal)
                        else:
                            print("entrada invalida, por favor digite uma das duas opções apresentadas")
                            continue
                        for tarefa in tarefas:
                            print(f"{tarefa}\n")

                case "5":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        tarefas = self._quadro.listar_tarefas()
                        if len(tarefas) == 0:
                            print("Não existem tarefas para remover, cadastre alguma antes de realizar a ação!")
                        else:
                            print("\n=== Tarefas a remover ===")
                            for i, tarefa in enumerate(tarefas, start=1):
                                print(f"{i}. {tarefa}\n")
                            indice = int(input("\nInsira a seguir o indice da tarefa que deseja remover: ").strip())
                            if 1 <= indice <= len(tarefas):
                                self._quadro.remover_tarefa(tarefas[indice - 1])
                                deletar_tarefa(tarefas[indice - 1].get_id())
                                print("Tarefa removida com sucesso!")
                            else:
                                print("Indice inválido")

                case "6": 
                    if not self.__verificar_quadro():
                        continue
                    else:
                        tarefas = self._quadro.listar_tarefas()
                        if len(tarefas) == 0:
                            print("\nNenhuma tarefa cadastrada")
                        else:
                            print("\n=== Tarefas === ")
                            for i, tarefa in enumerate(tarefas, start=1):
                                print (f"{i}. {tarefa.exibir_detalhes()}\n")
                            indice = int(input("\nInsira a seguir o indice da tarefa que deseja alterar o status para \"em andamento\": ").strip())
                            if 1<= indice <= len(tarefas):
                                tarefas[indice - 1].mover_para_andamento()
                                atualizar_status(tarefas[indice - 1].get_id(), "Em andamento")
                                print("Status alterado para \"em andamento\"!")
                            else:
                                print("Indice inválido")

                case "7":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        tarefas = self._quadro.listar_tarefas()
                        if len(tarefas) == 0:
                            print("\nNenhuma tarefa cadastrada")
                        else:
                            print("\n=== Tarefas === ")
                            for i, tarefa in enumerate(tarefas, start=1):
                                print (f"{i}. {tarefa.exibir_detalhes()}\n")
                            indice = int(input("\nInsira a seguir o indice da tarefa que deseja alterar o status para \"concluído\": ").strip())
                            if 1<= indice <= len(tarefas):
                                tarefas[indice - 1].mover_para_concluido()
                                atualizar_status(tarefas[indice - 1].get_id(), "Concluído")
                                print("Status alterado para \"concluído\"!")
                            else:
                                print("Indice inválido")

                case "8":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        for i, tarefa in enumerate(self._quadro.listar_tarefas(), start=1):
                            print(f"{i}. {tarefa}\n")

                case "9":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        for i, tarefa in enumerate(self._quadro.listar_tarefas(), start=1):
                            print (f"{i}. {tarefa.exibir_detalhes()}\n")
                        
                case "10":
                    if not self.__verificar_quadro():
                        continue
                    else:
                        tarefas = self._quadro.listar_tarefas()
                        for i, tarefa in enumerate(self._quadro.listar_tarefas(), start=1):
                            if isinstance(tarefa, TarefaAcademica):
                                print(f"{i}. {tarefa}")
                        indice = int(input("Insira a seguir o indice da tarefa que deseja verificar o prazo: "))
                        if 1<= indice <= len(tarefas):
                                print(tarefas[indice - 1].verificar_prazo())
                        else:
                            print("Indice invalido")

                case "11":
                    print("Encerrando sistema...")
                    break

                case _:
                    print("Opção inválida!\n")