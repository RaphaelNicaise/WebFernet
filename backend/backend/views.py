from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a Web Fernet</h1><p>Página principal del proyecto</p>")
