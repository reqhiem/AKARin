from django.urls import path

from myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home' ),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('buscar/', views.buscar, name="Buscar"),
    path('cargar/', views.cargar, name="Subir"),
    path('help/', views.help, name="Ayuda"),
    path('loading/', views.help, name="Subiendo"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)