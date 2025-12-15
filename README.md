# Meu Projeto Django

Projeto Django criado para aprendizado prático e progressivo do framework.


## Estrutura do Projeto
meuprojeto/
├── core/ # App principal do projeto
│ ├── migrations/
│ ├── templates/core/
│ │ ├── home.html
│ │ └── sobre.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── texts.py
│ ├── urls.py
│ └── views.py
├── meuprojeto/ # Configurações do projeto
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── templates/ # Templates globais
│ ├── base.html
│ └── index.html
├── db.sqlite3 # Banco de dados SQLite
├── manage.py # Script de administração do Django
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo

text

## Tecnologias Utilizadas

- **Django**: 4.2.27
- **Python**: 3.11.9
- **Banco de Dados**: SQLite3

## Funcionalidades

### App Core
- Modelos para gerenciamento de dados
- Views funcionais
- URLs configuradas
- Admin personalizado
- Formulários integrados

### Templates
- Base template (`base.html`)
- Página inicial (`index.html`)
- Página do app core (`home.html`, `sobre.html`)

## Como Executar

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv

Ative o ambiente virtual:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Instale as dependências:

bash
pip install -r requirements.txt
Execute as migrações:

bash
python manage.py migrate
Crie um superusuário (opcional):

bash
python manage.py createsuperuser
Inicie o servidor:

bash
python manage.py runserver
Acesse http://localhost:8000

Acesso
Página inicial: http://localhost:8000

Admin Django: http://localhost:8000/admin

App Core: http://localhost:8000/core

Sobre o Projeto
Projeto educativo desenvolvido para aprender Django de forma prática e gradual, implementando conceitos fundamentais do framework.
