from django import forms
from django.forms import extras

from Auth.models import User, Profile

import datetime

class ProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(1940, datetime.date.today().year+10)))

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'description',
            'profile_picture',
            'dob',
            'gender',
            'country',
            'city'
        )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
