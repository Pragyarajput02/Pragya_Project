from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobinfo(request):
    s='<h1>Hyderabad Job Information</h1>'
    return HttpResponse(s)
def punejobinfo(request):
    s='<h1>Pune Job Information</h1>'
    return HttpResponse(s)
def mumjobinfo(request):
    s='<h1>Mumbai Job Information</h1>'
    return HttpResponse(s)
def chnjobinfo(request):
    s='<h1>Chennai Job Information</h1>'
    return HttpResponse(s)
def bngjobinfo(request):
    s='<h1>Bangalore Job Information</h1>'
    return HttpResponse(s)
