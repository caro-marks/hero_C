"""manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from manager.views import ContratoViewSet, ContratosEmpresaListView, ContratosFuncionarioListView, EmpresaViewSet, FuncionarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empresas', EmpresaViewSet, basename='Empresas')
router.register('funcionarios', FuncionarioViewSet, basename='Funcionarios')
router.register('contratos', ContratoViewSet, basename='Contratos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('funcionario/<int:pk>/contratos/',
         ContratosFuncionarioListView.as_view()),
    path('empresa/<int:pk>/contratos/', ContratosEmpresaListView.as_view())
]
