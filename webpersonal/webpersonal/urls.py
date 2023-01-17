from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    #Rutas del navegador web las cuales se usan para acceder 
    # a las vistas guardadadas en las carpetas
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
    

]
