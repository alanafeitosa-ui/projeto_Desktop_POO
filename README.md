# 📌 Organizador de Tarefas e Estudos (Kanban)

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**, com o objetivo de aplicar conceitos fundamentais da orientação a objetos por meio da implementação de um sistema desktop para gerenciamento de tarefas acadêmicas e pessoais no estilo Kanban.

O projeto foi desenvolvido de forma incremental ao longo de quatro etapas, evoluindo desde a modelagem das classes até a implementação de persistência de dados e interface gráfica.

---

# ✨ Funcionalidades

- Cadastro de tarefas acadêmicas e pessoais
- Listagem de tarefas
- Remoção de tarefas
- Alteração de status das tarefas
- Exibição detalhada das informações de cada tarefa
- Filtragem de tarefas por tipo
- Persistência de dados utilizando SQLite
- Interface gráfica para interação com o sistema

---

# 🏛️ Arquitetura

O projeto foi organizado seguindo uma estrutura inspirada no padrão **MVC (Model-View-Controller)**.

```text
src/
├── database/
│   ├── conexao.py
│   └── tarefa_repository.py
├── models/
│   ├── quadro.py
│   ├── tarefa.py
│   ├── tarefa_academica.py
│   ├── tarefa_pessoal.py
│   └── usuario.py
├── views/
│   ├── menu.py
│   ├── componentes.py
│   └── janela_principal.py
└── main.py
```

---

# 🧩 Conceitos de POO aplicados

- Encapsulamento
- Herança
- Polimorfismo
- Abstração
- Classes abstratas
- Composição
- Tipagem com *type hints*
- Organização modular do código

---

# 💾 Persistência de Dados

A persistência das informações foi implementada utilizando **SQLite**, permitindo que as tarefas permaneçam armazenadas mesmo após o encerramento da aplicação.

O banco de dados é criado automaticamente quando necessário.

---

# 🖥️ Interface

O sistema possui:

- Menu interativo em terminal (Entrega 2)
- Interface gráfica desktop (Entrega 4)

A interface gráfica foi desenvolvida mantendo separação entre apresentação e lógica de negócio.

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- SQLite3
- Tkinter
- Git
- GitHub

---

# 📅 Evolução do Projeto

## Entrega 1
- Modelagem UML
- Implementação das classes
- Aplicação dos conceitos de Programação Orientada a Objetos

## Entrega 2
- Implementação do menu interativo
- Integração das funcionalidades
- Refatoração e organização da estrutura do projeto

## Entrega 3
- Implementação da persistência de dados
- Integração com SQLite
- Operações de CRUD

## Entrega 4
- Desenvolvimento da interface gráfica
- Integração da interface com a lógica da aplicação

---

# 🚀 Como executar

## Clone o repositório

```bash
git clone https://github.com/alanafeitosa-ui/projeto_Desktop_POO.git
```

## Acesse o projeto

```bash
cd projeto_Desktop_POO
```

## Execute a aplicação

```bash
python -m src.main
```

---

# 👥 Equipe

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos**.

- Alana Feitosa
- Yasmim Ayres

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.

---

# 📄 Status

✅ Projeto concluído.
