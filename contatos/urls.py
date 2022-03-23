from django.urls import path
from . import views


urlpatterns = [
    path('', views.contatos, name='contatos'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('<int:id>', views.contato, name='contato')
]
