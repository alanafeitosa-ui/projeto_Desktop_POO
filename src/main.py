from src.models.tarefa import TarefaAcademica, TarefaPessoal
from src.models.quadro import Quadro
meu_Quadro = Quadro("tarefas Semana 1")
tarefaAcademica1 = TarefaAcademica("Prova calculo 1", "Estudar conteudo de integrais", "Em andamento", "Calculo 1", "7/7/2026", "Urgente\n")
tarefaPessoal_1 = TarefaPessoal("Ir ao mercado", "Realizar as compras pro churrasco", "A concluir\n")
tarefaAcademica2 = TarefaAcademica("Lista de fisica", "Realizar lista extra", "Em andamento", "Fisica", "21/07/2026", "Media\n")
meu_Quadro.adicionar_tarefa(tarefaAcademica1)
meu_Quadro.adicionar_tarefa(tarefaAcademica2)
meu_Quadro.adicionar_tarefa(tarefaPessoal_1)
for i in meu_Quadro.listar_tarefas():
    print (i.exibir_detalhes())
print("\nTarefas Acadêmicas\n")
for i in meu_Quadro.filtrar_por_tipo(TarefaAcademica):
    print(i.exibir_detalhes())
meu_Quadro.remover_tarefa(tarefaAcademica2)
print("\nApós remoção da segunda tarefa acadêmica: \n")
for i in meu_Quadro.listar_tarefas():
    print (i.exibir_detalhes())
tarefaAcademica1.mover_para_andamento()
tarefaPessoal_1.mover_para_concluido()
print("\nApós alterações: \n")
for i in meu_Quadro.listar_tarefas():
    print (i.exibir_detalhes())
meu_Quadro.listar_tarefas()
