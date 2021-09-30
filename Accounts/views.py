'''

from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q

def home(request):
    template_name='Accounts/base.html'
    context={}
    return render(request,template_name,context)

def registrationView(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'Accounts/Register.html'
    context = {'form': form}
    return render(request, template_name, context)

def loginview(request):
    if request.method == 'POST':

        user_profile=request.POST.get('user_profile')
        MN = request.POST.get('mn')
        P = request.POST.get('ps')

        z = CustomUser.objects.filter(Q(mobile_no=MN) & Q(password=P) & Q(profile=user_profile))
        if z:
            for x in z:
                    if x.profile=='customer':
                        return redirect('customer-reg')
                    else:
                        return redirect('seller-reg')

        else:
            messages.error(request, 'Invalid Credentials')


'''
'''
        print(f'user profile:{user_profile},type:{type(user_profile)}')
        print(f'mobile number:{MN},type:{type(MN)}')
        print(f'password:{P},type:{type(P)}')

        z=CustomUser.objects.filter(Q(mobile_no=MN) & Q(password=P))
        print(f'z:{z},type:{type(z)}')
        for x in z:
            print(f'mobile no of object:{x.mobile_no},profile of object:{x.profile},type of profile:{type(x.profile)}')
 
        if CustomUser(mobile_no=MN,password=P):
            return redirect('customer-reg')
        else:
            return redirect('seller-reg')
   
        user = authenticate(username=U, password=P)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
'''
'''
    template_name = 'Accounts/Login.html'
    context = {}
    return render(request, template_name, context)

def customer_registrationView(request):
    form=CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'Accounts/customer_registration.html'
    context = {'form': form}
    return render(request, template_name, context)


def seller_registrationView(request):
    form=SellerForm()
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'Accounts/SellerRegister.html'
    context = {'form': form}
    return render(request, template_name, context)
'''
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout



def home(request):
    template_name='Accounts/base.html'
    context={}
    return render(request,template_name,context)

def home2(request):
    template_name='Accounts/base2.html'
    context={}
    return render(request,template_name,context)

def RegisterView(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'Accounts/Register.html'
    context = {'form': form}
    return render(request, template_name, context)


def LoginView(request):
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_customer:
            login(request, user)
            return redirect('show')
        messages.error(request, 'You are not a customer')
    template_name = 'Accounts/Login2.html'
    context = {}
    return render(request, template_name, context)


def ShowView(request):
    usr = Customer.objects.all()
    print(usr)
    tempalte_name = 'Accounts/Show.html'
    context = {'user': usr}
    return render(request, tempalte_name, context)


def SellerRegisterView(request):
    form = SellerCreationForm()
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellerlogin')
    template_name = 'Accounts/SellerRegister.html'
    context = {'form': form}
    return render(request, template_name, context)


def SellerLoginView(request):
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_seller:
            login(request, user)
            return redirect('sellershow')
        messages.error(request, 'You are not a Seller')
    template_name = 'Accounts/SellerLogin.html'
    context = {}
    return render(request, template_name, context)


def SellerShowView(request):
    usr = Seller.objects.all()
    print(usr)
    tempalte_name = 'Accounts/SellerShow.html'
    context = {'user': usr}
    return render(request, tempalte_name, context)


