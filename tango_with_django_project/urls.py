from django.contrib import admin
from django.urls import path
from django.url import include
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('rango/', include('rango.urls')),
    # the above maps any URLs starting with rango/ to be handled by rango
    path('admin/', admin.site.urls),
]
