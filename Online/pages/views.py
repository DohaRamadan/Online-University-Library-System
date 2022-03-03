from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

slug_url_kwarg = 'slug'


# Create your views here.
def index(request):
    return render(request, 'index.html')


def books(request):
    searchf = Book.objects.all()
    if request.method == 'POST':

        cat = request.POST['category']

        if cat == 'ISBN':
            isbn = None
            if 'search' in request.POST:
                isbn = request.POST['search']
                if isbn:
                    searchf = searchf.filter(isbn=isbn)

        elif cat == 'Title':
            title = None
            if 'search' in request.POST:
                title = request.POST['search']
                if title:
                    searchf = searchf.filter(title__icontains=title)

        elif cat == 'Author':
            author = None
            if 'search' in request.POST:
                author = request.POST['search']
                if author:
                    searchf = searchf.filter(author__icontains=author)


        elif cat == 'Year':
            Year = None
            if 'search' in request.POST:
                Year = request.POST['search']
                if Year:
                    searchf = searchf.filter(publication_year=Year)

    context = {
        'books': searchf,
        'category': Category.objects.all()
    }
    return render(request, 'books.html', context)

# @unauthenticated_user
@csrf_exempt
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('pages:index')
    return render(request, 'signup.html', {
        'form': form
    })


def login(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('pages:index')


    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })


@csrf_exempt
def addbook(request):
    if request.method == 'POST':
        add_book = AddBookForm(request.POST)
        if add_book.is_valid():
            add_book.save()
            return redirect('pages:books')
    context = {
        'books': Book.objects.all(),
        'form': AddBookForm()
    }
    return render(request, 'addbook.html', context)


@login_required(login_url='pages:login')
def updateUser(request):
    if request.method == 'POST':
        user_profile = UserUpdate(request.POST, instance=request.user)
        if user_profile.is_valid():
            user_profile.save()
            return redirect('pages:index')
    else:
        user_profile = UserUpdate(instance=request.user)
    return render(request, 'updateuser.html', {
        'profile': user_profile
    })


def bookdetails(request, slug):
    book_details = Book.objects.get(slug=slug)
    return render(request, 'bookdetails.html', {
        'book_details': book_details
    })


@csrf_exempt
def updatebook(request, slug):
    book_id = Book.objects.get(slug=slug)
    if request.method == 'POST':
        book_save = UpdateBookForm(request.POST, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('pages:books')
    else:
        book_save = UpdateBookForm(instance=book_id)
    context = {
        'form': book_save,
        'books': Book.objects.all()
    }
    return render(request, 'updatebook.html', context)


@login_required(login_url='pages:login')
def logout(request):
    auth.logout(request)
    return redirect('pages:index')


def borrow(request, slug):
    book = Book.objects.get(slug=slug)
    if book.status == 'Available':
        book.__setattr__('status', 'Borrowed')
        book.save()
    return render(request, 'borrowbook.html')

def returnbook(request, slug):
    book = Book.objects.get(slug=slug)
    if book.status == 'Borrowed':
        book.__setattr__('status', 'Available')
        book.save()
    return render(request, 'returnbook.html')

def extendbook(request, slug):
    book = Book.objects.get(slug=slug)
    if book.borrowing_period < 20 and book.status == 'Borrowed' :
        book.__setattr__('borrowing_period',  book.borrowing_period +5)
        book.save()
    return render(request, 'extend.html')
