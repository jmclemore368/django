from django.http import HttpResponse

def index(request):
    # include link to about page
    return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")

def about(request):
    # include link to about page
    return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")