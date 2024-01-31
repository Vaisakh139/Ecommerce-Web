from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address') 
            password = request.POST.get('password')  
    ##create user accounts
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
    ##create customer accounts
            customer = Customer.objects.create(
                user = user,
                phone = phone,
                address = address
            )
            sucess_msg = "Register is success"
            messages.success(request, sucess_msg)
        except Exception as e:
            error_msg = "failed"
            messages.error(request, error_msg)
        
    if request.POST and 'login' in request.POST:
        context['register'] = False

        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('list_products')
        else:
             messages.error(request, 'not a user')
    return render(request,'account.html',context)