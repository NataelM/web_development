"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from proyecto1.views import saludo, despedida, dame_fecha, calcula_edad, video_yt, equipo #importando el archivo .py que trae las funciones saludo

urlpatterns = [
    path("admin/", admin.site.urls),
    # la primera entrada es el nombre con el que se busca el response en la página web,
    # la segunda entrada es el nombre de la función dentro del codigo
    path('saludo/', saludo), #aquí se manda a llamar la función vista que vive en views.py llamada 'saludo'
    path('adios/', despedida),
    path('fecha/', dame_fecha),
    #dado que la url ahora recibira un parametro
    # y ese parametro debe de ser un entero, eso se declara así
    # '<int:anio>' int indica que ese parametro será de tipo entero
    path('edades/<int:edad>/<int:anio>', calcula_edad),
    path('video/', video_yt),
    path('equipo/', equipo),
]

