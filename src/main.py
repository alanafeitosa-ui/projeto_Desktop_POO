from src.models.tarefa import TarefaAcademica, TarefaPessoal
from src.models.quadro import Quadro
meu_Quadro = Quadro("tarefas Semana 1", "Todas")
tarefaAcademica1 = TarefaAcademica("Prova calculo 1", "Estudar sonteudo de integrais", "Em andamento", "Calculo 1", "7/7/2026", "Urgente")
tarefaPessoal_1 = TarefaPessoal("Ir ao mercado", "Realizar as compras pro churrasco", "A concluir")
meu_Quadro.adicionar_tarefa(tarefaAcademica1)
meu_Quadro.adicionar_tarefa(tarefaPessoal_1)
for i in meu_Quadro.listar_tarefas():
    print (i.exibirDetalhes())
    print (i.exibirDetalhes())