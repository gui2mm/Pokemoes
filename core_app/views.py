from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.

class ViewCore(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html')
