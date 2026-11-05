from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)
from django.contrib.auth.models import User

from .models import EmployeeModel


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = EmployeeModel
        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter employee name"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter age"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Department"
            }),

            "salary": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Salary"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Address"
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            })
        }


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))


class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))