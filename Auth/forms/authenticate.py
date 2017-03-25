from django import forms
from django.contrib.auth import authenticate

from Auth.models import User

class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Sorry, those details don't belong to anyone. Make sure you've spelled everything correctly.")
        if not user.is_active:
            raise forms.ValidationError('Your account has been disabled.')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user
