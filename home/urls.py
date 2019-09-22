from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_welcome(), name='show_welcome')
]