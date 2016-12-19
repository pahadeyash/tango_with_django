from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")# Create your views here.

def about(request):
	return HttpResponse("Rango says hello world! <a href='/rango/'>Index</a>")
