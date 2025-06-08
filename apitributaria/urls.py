# apitributaria/urls.py 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('servicios.urls')),  # Aquí es donde Django debe encontrar las rutas de API
]



