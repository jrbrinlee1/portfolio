from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funky', views.funky, name='funky'),
    path('danger', views.danger, name='danger'),
]
