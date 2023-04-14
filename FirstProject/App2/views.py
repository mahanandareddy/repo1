from django.shortcuts import render
from django.http import HttpResponse
import datetime
def f22(request):
    time=datetime.datetime.now()
    msg='<h2>Hello user..!<br/><br/>Server Date & time:: '+str(time)+'</h2><hr/>'
    return HttpResponse(msg)