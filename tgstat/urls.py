from django.urls import path
from webstat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('longest/', views.upload_file, name='longest'),
]