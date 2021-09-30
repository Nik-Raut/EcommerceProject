'''
from django.urls import path
from . views import *

urlpatterns = [
    path('',home,name='home'),
    path('reg/',registrationView,name='reg'),
    path('login/', loginview, name='login'),
    path('customer-reg/', customer_registrationView, name='customer-reg'),
    path('seller-reg/', seller_registrationView, name='seller-reg'),

]
'''
from django.urls import path
from .views import *



urlpatterns=[
    path('home/',home,name='home'),
    path('home2/', home2, name='home2'),
    path('reg/',RegisterView,name='register'),
    path('log/',LoginView,name='login'),
    path('show/',ShowView,name='show'),
    path('sreg/',SellerRegisterView,name='sellerregister'),
    path('slog/',SellerLoginView,name='sellerlogin'),
    path('sshow/',SellerShowView,name='sellershow'),
]
