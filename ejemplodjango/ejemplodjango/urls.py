"""ejemplodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplodjango.views import saludo, despedida, give_date, calcula_edad, hija, hija_dos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saluditos/', saludo),
    path('adios/', despedida),
    path('fecha/', give_date),
    path('edades/<int:edad>/<int:ano>', calcula_edad),
    path('hija/', hija),
    path('hijados/', hija_dos),
]
