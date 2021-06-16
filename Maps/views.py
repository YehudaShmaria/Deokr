from django.shortcuts import render,  HttpResponse

# Create your views here.

def Maps(request):
    return render(request,'maps/all.html')

def Detailes(request):
    return render(request,'maps/detailes.html')