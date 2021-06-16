from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Curtain

def All(request):
    Obj = Curtain.objects.all()
    my_context = {
        "Vilons":Obj
    }
    return render(request,'vilon/all.html',my_context)

def VilonTfira(request):
    Obj = Curtain.objects.all().filter(type='tefira')
    my_context = {
        "Vilons":Obj
    }
    return render(request,'vilon/tfira.html',my_context)

def VilonZebra(request):
    Obj = Curtain.objects.all().filter(type='zebra')
    my_context = {
        "Vilons":Obj
    }
    return render(request,'vilon/zebra.html',my_context)

def VilonRoma(request):
    Obj = Curtain.objects.all().filter(type='roma')
    my_context = {
        "Vilons":Obj
    }
    return render(request,'vilon/roma.html',my_context)

def VilonVan(request,name):
    Obj = {}
    temp = ''
    if name == 'e':
        temp = 'עץ'
    if name == 'de':
        temp = 'דמוי עץ'
    if name == 'alu':
        temp = 'אלומיניום'
    if name == 'empti':
        Obj = Curtain.objects.all().filter(type='van')
    else:
        Obj = Curtain.objects.all().filter(type='van',name = temp)
    my_context = {
        "Vilons":Obj
    }
    return render(request,'vilon/van.html',my_context)



def Detailes(request,id):
    Obj = get_object_or_404(Curtain,id=id)
    context = {
        "MyObj":Obj
    }
    return render(request,'vilon/detailes.html',context)
