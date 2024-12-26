from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
    path('intro', views.intro_page, name='intro'),
    path('overview/', views.overview, name='overview'),
]
