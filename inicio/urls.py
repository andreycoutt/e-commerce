from django.urls import path, include
from . import views

urlpatterns = [
    path('helloworld', views.helloWorld),
    path('', views.PagInicial, name="Pagina-Inicial"),
]