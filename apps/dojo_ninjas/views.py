from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    return render(request, "dojo_ninjas/index.html")
