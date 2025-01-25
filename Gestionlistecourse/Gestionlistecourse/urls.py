from django.contrib import admin
from django.urls import path, include  # Ajoutez include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),  # Incluez les URLs de l'application
]
