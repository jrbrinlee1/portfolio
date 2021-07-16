from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 127.0.0.1:8000/trial
def index(request):
    return HttpResponse("Hello, world. You're at the trial index.")


# 127.0.0.1:8000/trial/funky
def funky(request):
    return HttpResponse("""<html><body><p>This is the funky function sample</p></body><html>""")


# 127.0.0.1:8000/trial/danger?guess=45
def danger(request):
    return HttpResponse("""<html><body><p>Your guess was """ + request.GET['guess'] + """</p></body></html>""")