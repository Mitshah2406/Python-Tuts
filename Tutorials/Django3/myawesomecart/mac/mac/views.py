from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('''<h1><a href="/shop" target="blank">Go To Shop</a></h1> <br><h1><a href="/admin" target="_blank">Go To Admin</a></h1>''')
