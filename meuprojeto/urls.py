# meuprojeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # ← Importar render
import sys  # ← Para pegar versão do Python

def home_view(request):
    context = {
        'django_version': '4.2.27',  # Sua versão do Django
        'python_version': sys.version.split()[0],  # Versão do Python
    }
    return render(request, 'index.html', context)  # ← Usar template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('core/', include('core.urls')),
]