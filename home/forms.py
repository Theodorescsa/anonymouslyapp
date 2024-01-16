from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    
    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            
            if password2 and password == password2:
                return password
            raise forms.ValidationError('Passwords do not match')
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username khong hop le hoac da ton tai')
    def save(self):
        User.objects.create_user(

            username = self.cleaned_data['username'],

            password = self.cleaned_data['password'],
        )
    
    
            
    