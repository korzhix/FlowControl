from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "mainApp/disk.html")

def login_page(request):
	return render(request, 'mainApp/login.html')

def disk_page(request):
	return render(request, 'mainApp/disk.html')