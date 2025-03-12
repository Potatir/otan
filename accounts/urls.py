from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('logout/', views.custom_logout, name='logout'),
]