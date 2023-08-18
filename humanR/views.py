from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse

def contact(request):
  return render(request, 'contact.html')
def register(request):
  return render(request, 'register.html') 
def login(request):
  return render(request, 'login.html')
def index(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def attendance(request):
  return render(request, 'attendance.html')
def report(request):
  return render(request, 'report.html')


