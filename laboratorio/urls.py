from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),  # Redirigir al login
    path('laboratorios/', views.laboratorio_list, name='laboratorio_list'),
    path('laboratorios/<int:id>/', views.laboratorio_detail, name='laboratorio_detail'),
    path('laboratorios/create/', views.laboratorio_create, name='laboratorio_create'),
    path('laboratorios/<int:id>/update/', views.laboratorio_update, name='laboratorio_update'),
    path('laboratorios/<int:id>/delete/', views.laboratorio_delete, name='laboratorio_delete'),
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/<int:id>/', views.producto_detail, name='producto_detail'),
    path('directores/', views.director_list, name='director_list'),
    path('directores/<int:id>/', views.director_detail, name='director_detail'),
]