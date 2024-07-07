from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , "index.html")

def laptop(request):
    return render(request , "laptop.html")
def contact(request):
    return render(request , "contact.html")
def computer(request):
    return render(request , "computer.html")
def about(request):
    return render(request , "about.html")
