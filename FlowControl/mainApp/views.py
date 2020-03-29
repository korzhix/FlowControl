from django.shortcuts import render

from accountApp.models import Profile
# Create your views here.

def index(request):
	if request.user.pk is not None:
		student = student = Profile.objects.get(pk=request.user.pk)
		return render(request, "mainApp/disk.html", {'student': student})
	return render(request, 'mainApp/disk.html')

def disk_page(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		return render(request, "mainApp/disk.html", {'student': student})

	return render(request, 'mainApp/disk.html')
