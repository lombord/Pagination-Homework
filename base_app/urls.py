from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
]
