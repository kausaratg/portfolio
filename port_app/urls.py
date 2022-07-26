from django.urls import path
from port_app import views


urlpatterns = [
    path('', views.index, name='index'),
]
