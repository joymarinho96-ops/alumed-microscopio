from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # AQUI ESTÁ O COMANDO: Trocamos 'index.html' pelo nome do seu arquivo
    path('', TemplateView.as_view(template_name='microscopio_deepzoom.html')),
]
