'''
from django import forms
from .models import *

class CustomUserForm(forms.ModelForm):
    mobile_no=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    choice=(('customer','Customer'),('seller','Seller'))
    profile=forms.ChoiceField(choices=choice,widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields='__all__'

        labels = {
            'mobile_no': 'User Name',
            'password': 'Password',
            'password_confirm': 'Confirm Password',
            'is_customer':'Customer',
            'is_seller':'Seller',
        }

    def clean(self):
        cleaned_data = super(CustomUserForm, self).clean()
        mobile=cleaned_data.get('mobile_no')
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_confirm")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        elif len(str(mobile))<10 or len(str(mobile))>10:
            raise forms.ValidationError(
                "Mobile Number should be of 10 digits"
            )
'''
'''
    def clean_mobile_no(self):
        z = self.cleaned_data['mobile_no']
        if len(str(z))< 10 or len(str(z))>10:
            raise forms.ValidationError('Mobile Number should be of 10 digits')
        return z
'''
'''
class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Customer
        fields='__all__'

    def clean(self):
        cleaned_data = super(CustomerForm, self).clean()
        mobile=cleaned_data.get('mobile_no')

        if len(str(mobile))<10 or len(str(mobile))>10:
            raise forms.ValidationError(
                "Mobile Number should be of 10 digits"
            )

class SellerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Seller
        fields='__all__'

    def clean(self):
        cleaned_data = super(SellerForm, self).clean()
        mobile = cleaned_data.get('mobile_no')

        if len(str(mobile))< 10 or len(str(mobile))> 10:
            raise forms.ValidationError(
                "Mobile Number should be of 10 digits"
            )
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer, Seller


class CustomerCreationForm(UserCreationForm):
    name=forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ('mobile_no','email')

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        nm=self.cleaned_data.get('name')
        customer = Customer.objects.create(user=user,name=nm)
        return user

class SellerCreationForm(UserCreationForm):
    company_name=forms.CharField(max_length=50)
    gst_no=forms.CharField(max_length=200)
    address=forms.CharField(max_length=1000)
    bank_account=forms.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('mobile_no','email')

    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        a=self.cleaned_data.get('address')
        b=self.cleaned_data.get('bank_account')
        c=self.cleaned_data.get('company_name')
        g=self.cleaned_data.get('gst_no')
        customer = Seller.objects.create(user=user,company_name=c,gst_no=g,address=a,bank_account=b)
        return user