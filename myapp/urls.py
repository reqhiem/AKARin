from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = [
    path('', views.home, name='Home' ),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('buscar/', views.buscar, name="Buscar"),
    path('cargar/', views.cargar, name="Subir"),
    path('help/', views.help, name="Ayuda"),
    path('loading/', views.help, name="Subiendo"),
    path('perfile/', views.perfile, name="Perfile"),
    path('eliminar/<id>/', views.eliminar, name="Eliminar"),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='myapp/login.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)