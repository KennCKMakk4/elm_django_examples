from django.shortcuts import render
from django.http import HttpResponse

def get_view(request):
    get_dict = request.GET
    name     = get_dict.get("name","")
    age      = get_dict.get("age","")

    return HttpResponse("Hello " + name + " you're " + age + " years old")

def post_view(request):
    post_dict = request.POST
    name     = post_dict.get("name","")
    age      = post_dict.get("age","")

    return HttpResponse("Hello " + name + " you're " + age + " years old")
