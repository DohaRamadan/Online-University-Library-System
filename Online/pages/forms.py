from django.contrib.auth import models
from django.forms import widgets
from django.forms.fields import CharField
from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from django.db.models import fields
from datetime import date
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(widget=widgets.TextInput(attrs={'id': 'first_name_input_field'}))
    last_name = forms.CharField(widget=widgets.TextInput(attrs={'id': 'last_name_input_field'}))
    username = forms.CharField(widget=widgets.TextInput(attrs={'id': 'username_input_field'}))
    email = forms.EmailField(widget=widgets.EmailInput(attrs={'id': 'email_input_field'}))
    password1 = forms.CharField(widget=widgets.PasswordInput(attrs={'id': 'password1_input_field'}))
    password2 = forms.CharField(widget=widgets.PasswordInput(attrs={'id': 'password2_input_field'}))


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'borrowing_period', 'publication_year', 'status']

    book_status = [
        ('Available', 'Available'),
        ('Borrowed', 'Borrowed'),
    ]
    title = forms.CharField(max_length=250, widget=forms.TextInput)
    author = forms.CharField(max_length=250, widget=forms.TextInput)
    borrowing_period = forms.CharField(required=False)
    publication_year = models.IntegerField()
    isbn = forms.CharField(max_length=10, widget=forms.TextInput)
    status = forms.ChoiceField(widget=forms.Select(attrs={'id': 'st'}), choices=book_status)


class UpdateBookForm(forms.ModelForm):
    book_status = [
        ('Available', 'Available'),
        ('Borrowed', 'Borrowed'),
    ]
    status = forms.ChoiceField(widget=forms.Select(attrs={'id': 'status'}), choices=book_status)

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'borrowing_period', 'publication_year', 'status']
