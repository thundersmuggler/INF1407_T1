from django.urls.conf import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.UsuarioListView.as_view(), name='lista-usuarios'),
    path('', views.UsuarioListView.as_view(), name='home-usuarios'),]