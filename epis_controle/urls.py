"""
URL configuration for epis_controle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from home.views import home, cadastrar_colaborador, editar_colaborador, excluir_colaborador, relatorio, cadastrar_equipamento, editar_equipamento, excluir_equipamento, listar_equipamentos
from home.views import controle_epi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('colaboradores/cadastrar/', cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/<int:pk>/editar/', editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:pk>/excluir/', excluir_colaborador, name='excluir_colaborador'),
    path('relatorio/', relatorio, name='relatorio'),
    path('equipamentos/cadastrar/', cadastrar_equipamento, name='cadastrar_equipamento'),
    path('equipamentos/<int:pk>/editar/', editar_equipamento, name='editar_equipamento'),
    path('equipamentos/<int:pk>/excluir/', excluir_equipamento, name='excluir_equipamento'),
    path('equipamentos/listar/', listar_equipamentos, name='listar_equipamentos'),
    path('controle-epi/', controle_epi, name='controle_epi'),
    path('controle-epi/<int:pk>/', controle_epi, name='editar_controle_epi'),
]
