from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ShowMsg(request):
    return HttpResponse("Welcome to my webpage")















def Homepage(request):
    return render(request,'Homepage.html')
def valuePage(request):
    dic1={
        'name':'django jinja formate'
    }
    return render(request,'jinjapage.html',dic1)