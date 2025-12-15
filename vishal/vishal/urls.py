from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]