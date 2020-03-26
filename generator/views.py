from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    chars = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        chars.extend([c.upper() for c in chars])
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    passwrd = ''
    for x in range(length):
        passwrd += random.choice(chars)

    return render(request, 'generator/password.html', {'password':passwrd})

def about(request):
    return render(request, 'generator/about.html')