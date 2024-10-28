

# TudoList - Plataforma de Gerenciamento de Estudos Universitários
TudoList é uma ferramenta desenvolvida para ajudar estudantes a gerenciar de maneira eficiente e organizada seus compromissos acadêmicos. Com uma interface amigável e funcionalidades personalizáveis, a plataforma visa otimizar a experiência de estudos, garantindo que todos possam acessar e utilizar a plataforma, independentemente de suas necessidades linguísticas ou de acessibilidade.

Desenvolvido por: Ana Carolina Torchia de Souza


## Índice

- [Funcionalidades](#funcionalidades)
- [Uso](#uso)


## Funcionalidades

- **Organização de Tarefas:** Adicione, categorize, edite e acompanhe suas tarefas acadêmicas.
- **Gerenciamento de Horários:** Visualize e gerencie seu calendário de aulas e eventos acadêmicos.
- **Registro de Notas e Progresso Acadêmico:** Registre suas notas e acompanhe seu progresso ao longo do semestre.
- **Personalização de Idioma:** Mude o idioma da interface da plataforma para atender suas preferências linguísticas.

## JIRA

Board com backlog e items para sprint


## Protótipos

- Cadastro - Jira e Figma

- Login -
- ![Captura de tela_27-10-2024_222122_127 0 0 1](https://github.com/user-attachments/assets/8a8b42ff-deda-4eeb-804b-96e993ebca1d)



- Editar dados do usuário - Jira e Figma



- Organização de Tarefas - Jira e Figma



- Progresso Acadêmico -
-  ![Captura de tela_27-10-2024_231358_127 0 0 1](https://github.com/user-attachments/assets/86404dab-4b8a-42b5-9afe-ee96d083a578)




- ScreenCast da plataforma:

### 💻 Como rodar o projeto na sua máquina:

O que você deve fazer ao entrar no projeto pela primeira vez:

> pip install virtualenv (caso não tenha o virtualenv instalado)

1- Criação do ambiente virtual:

> py -m venv .venv ou python -m venv .venv

2- Ativação do amb. virtual:

> .\.venv\Scripts\activate

3- Instalação do django:

> pip install django

3.1 -  Se não foram criadas as migrações dos seus models execute:

> python manage.py makemigrations

3.2 - Se sim execute:

> python manage.py migrate

4- Para rodar o servidor:

> python manage.py runserver <br> http://127.0.0.1:8000/
