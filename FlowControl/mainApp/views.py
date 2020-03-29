from django.shortcuts import render

from accountApp.models import Profile
# Create your views here.

def index(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		schadule_list = student.schadule.split('SEP')
		if len(schadule_list) <= 1:
			return render(request, 'mainApp/disk.html', {'schadule_list': []})

		else:
			return render(request, 'mainApp/disk.html', {'schadule_list': schadule_list[1:]})

	return render(request, 'mainApp/disk.html', {})

	return render(request, 'mainApp/disk.html')

def disk_page(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		schadule_list = student.schadule.split('SEP')
		if len(schadule_list) <= 1:
			return render(request, 'mainApp/disk.html', {'schadule_list': []})

		else:
			return render(request, 'mainApp/disk.html', {'schadule_list': schadule_list[1:]})

	return render(request, 'mainApp/disk.html')
