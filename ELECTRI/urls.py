
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # URL para el index.html
    path('solicitar/', views.solicitar_view, name='solicitar'),  # URL para solicitar.html
    # Otros paths aquí si los tienes
]
