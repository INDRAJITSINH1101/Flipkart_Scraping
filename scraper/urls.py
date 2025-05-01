from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('run-scraper/', views.run_scraper, name='run_scraper'),
]
