from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return HttpResponse("<h1>Sorry !! You need to authenticate yourself and then you can access your system.</h1>")
