from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100, label='' ,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'})
    )

    last_name = forms.CharField(
        max_length=100, label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام حانوادگی خود را وارد کنید'})
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
    )

    username = forms.CharField(
        max_length=100, label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'})
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control' ,
                   'placeholder': 'گذزواژه',
                   'name':'password',
                    'type': 'password'
            }
        )

    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'تکرار گذزواژه',
                   'name': 'password',
                   'type': 'password'
            }
        )

    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')    #به ترتیبی که میخواهم نمایش داده شود نوشته میشود

class UpdateUserForm(UserChangeForm):
    password=None

    first_name = forms.CharField(
        max_length=100, label='' ,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'})
    )

    last_name = forms.CharField(
        max_length=100, label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام حانوادگی خود را وارد کنید'})
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
    )

    username = forms.CharField(
        max_length=100, label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'})
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control' ,
                   'placeholder': 'گذزواژه',
                   'name':'password',
                    'type': 'password'
            }
        )

    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'تکرار گذزواژه',
                   'name': 'password',
                   'type': 'password'
            }
        )

    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')    #به ترتیبی که میخواهم نمایش داده شود نوشته میشود