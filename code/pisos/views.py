from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pisos(request):
    return render(request, 'index.html', {'welcome_text': 'Welcome to AlquiPiso!'})