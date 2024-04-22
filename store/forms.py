from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # fields = ('username','email','password')
        fields = ['username','email','password1','password2']
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'login__input'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'login__input'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login__input'}))