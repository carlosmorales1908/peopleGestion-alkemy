from django.urls import path
from compra import views

urlpatterns = [
    path('', views.home, name='home'),
]