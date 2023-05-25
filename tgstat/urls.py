from django.urls import path
from webstat import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)