from django.shortcuts import render
from django.utils import timezone
from .models import Post # работа с бд и с шаблонами базы данных 

# Create your views here.

def main_site(request):   
    return render(request,'main_site/index.html',{})

def doc_info(request):
    return render(request,'doc_info/index.html',{}) # ввывод сайта на страничке

def economic_info(request):
    return render(request,'economic_info/index.html',{})

def contact_info(request):
    return render(request,'contact_info/index.html',{}) 