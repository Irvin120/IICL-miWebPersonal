from django.shortcuts import render
#Este método que nos permite contestar a una petición devolviendo un código
from django.shortcuts import render, HttpResponse


#Funcion home este redirige a la vista home.html
def home(request):
 return render(request, "core/home.html")

#Funcion about este redirige a la vista about.html
def about(request):
 return render(request, "core/about.html")

#Funcion about este redirige a la vista portafolio.html
def portfolio(request):
 return render(request, "core/portfolio.html")

#Funcion about este redirige a la vista contac.html
def contact(request):
 return render(request, "core/contact.html")

