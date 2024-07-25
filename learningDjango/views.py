from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # here i have to add request at request i have to return http response
    # return HttpResponse("hello world you are in my  home page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("hello world you are in my about page")

def contact_page(request):
    return HttpResponse("hello world you are in my contact page")