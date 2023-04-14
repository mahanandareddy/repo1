from django.shortcuts import render
from django.http import HttpResponse
def f1(request):
    return HttpResponse('<h2>Good morning users have a niceday..!</h2><hr/>')
def f2(request):
    return HttpResponse('<h3>Good afternoon user hope you are doing grate<h3><hr/>')
def f3(request):
    return HttpResponse('<h4>Good evening how was your day<h4><hr/>')
    