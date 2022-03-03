from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('addbook/', views.addbook, name='addbook'),
    path('updateuser/', views.updateUser, name='updateuser'),
    path('logout/', views.logout, name='logout'),
    path('extendbook/<slug:slug>', views.extendbook, name="extend"),
    path('bookdetails/<slug:slug>', views.bookdetails, name='bookdetails'),
    path('updatebook/<slug:slug>', views.updatebook, name='updatebook'),
    path('borrow/<slug:slug>', views.borrow, name="borrow"),
    path('returnbook/<slug:slug>', views.returnbook, name="return"),
]
