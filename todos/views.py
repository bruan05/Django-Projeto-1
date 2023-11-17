from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Seja bem vindo ao projeto!!!")
    return render(request, "todos/home.html")
