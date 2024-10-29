from django.urls import path # type: ignore
from app_cad_usuarios import views
urlpatterns = [
   path('',views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
