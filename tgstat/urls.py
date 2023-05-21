from django.urls import path
from webstat import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('longest/', views.upload_file, name='longest'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)