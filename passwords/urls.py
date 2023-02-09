from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PasswordsView.as_view(), name="home"),
    path('delete/', views.deletePasswordView, name="delete_password")
]