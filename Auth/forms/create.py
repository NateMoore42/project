import re

from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm

from Auth.models import User, Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError('Your password is too short.')
        self.instance.username = self.cleaned_data.get('username')
        return password

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        taken = User.objects.filter(username__iexact=username)
        if re.match(r'^[A-Za-z]\w+$', username) is None:
            raise forms.ValidationError('Letters a-Z and numbers 0-9 only.')
        if taken:
            raise forms.ValidationError('That username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        taken = User.objects.filter(email=email)
        if taken:
            raise forms.ValidationError('That email address is already in use.')
        return email.lower()

class ProfileCreate(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'description',
            'dob',
            'gender',
            'profile_picture',
            'country',
            'city'
        )
