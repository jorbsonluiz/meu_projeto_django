# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def sobre(request):
    context = {
        'projeto': 'Meu Projeto Django',
        'autor': 'Jorbson Luiz 👨🏻‍💻',
        'ano': 2025,
        'tecnologias': ['Python', 'Django', 'Bootstrap', 'SQLite']
    }
    return render(request, 'core/sobre.html', context)