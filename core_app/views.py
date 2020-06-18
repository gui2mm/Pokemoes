from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import *

# Create your views here.

class ViewHome(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html')

class ViewLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'login.html')