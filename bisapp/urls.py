from django.urls import path
from .views import homepage,index,books,cart,login,contact

urlpatterns = [
    path('homepage/', homepage),
    path('index/', index),
    path('books/', books),
    path('contact/', contact),
    path('cart/', cart),
    path('login/', login)
]