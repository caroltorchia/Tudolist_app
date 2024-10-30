"""summary

    Raises:
        forms.ValidationError: description

    Returns:
        type: description
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nome",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu Nome"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu Sobrenome"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "example@email.com"}
        ),
    )
    instituicao = forms.CharField(
        max_length=100,
        required=False,
        label="Instituição de Ensino",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Instituição de Ensino"}
        ),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "****"}
        ),
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "****"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "instituicao",
            "email",
            "password1",
            "password2",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.instituicao = self.cleaned_data["instituicao"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "example@email.com"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Senha"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]
