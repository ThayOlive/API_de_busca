
from django.contrib import admin
from django.urls import path
from core.views import RegistrosView, SeachView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registros', RegistrosView.as_view(), name="registros"),
    path('api/registros/buscar/', SeachView.as_view(), name="busca_registro")
]
