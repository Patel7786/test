from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'name':'sankat'})

def add(request):
    p=int(request.GET['num1'])
    q=int(request.GET['num2'])
    res= p + q
    
    return render(request,'result.html',{'result':res})