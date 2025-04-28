from django import forms
from django.contrib.auth.models import User

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("This username is already taken.")
    return username

def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("This email is already associated with another account.")
    return email    
