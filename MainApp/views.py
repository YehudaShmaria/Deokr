from django.shortcuts import redirect, render,  HttpResponse
from django.core.mail import send_mail

# Create your views here.

def Home(request):
    return render(request,'main/home.html')

def About(request):
    return render(request,'main/about.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'name:{name} email: {email} phone: {phone} message: {message}')
        send_mail(name, phone +' '+ message, email, ['yehudas1999@gmail.com'])
        return render(request,'main/about.html')
    else:
        return render(request,'main/contact.html')