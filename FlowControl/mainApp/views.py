from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accountApp.models import Profile
from accountApp.models import Settings
# Create your views here.

def index(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		schadule = student.schadule[2:-2].replace('"','').split(',')
		if len(schadule) <= 1:
			return render(request, 'mainApp/disk.html', {'schadule': []})

		else:
			return render(request, 'mainApp/disk.html', {'schadule': schadule})

	return render(request, 'mainApp/disk.html', {})

	return render(request, 'mainApp/disk.html')

def disk_page(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		schadule = student.schadule[2:-2].replace('"','').split(',')
		settings = Settings.objects.get(pk=request.user.pk)
		disk_url = settings.url_of_disk
		if len(schadule) <= 1:
			return render(request, 'mainApp/disk.html', {'schadule': []})

		else:
			return render(request, 'mainApp/disk.html', {'schadule': schadule, 'disk_url': disk_url})

	return render(request, 'mainApp/disk.html')

def display_notes(request):
	if request.user.pk is not None:
		student = Profile.objects.get(pk=request.user.pk)
		schadule = student.schadule[2:-2].replace('"','').split(',')
		settings = Settings.objects.get(pk=request.user.pk)
		notes_url = settings.url_of_notes

		if len(schadule) <= 1:
			return render(request, 'mainApp/notes.html', {'schadule': []})

		else:
			return render(request, 'mainApp/notes.html', {'schadule': schadule, 'notes_url': notes_url})

	return render(request, 'mainApp/notes.html')

@login_required
def brs_view(request):
	student = Profile.objects.get(pk=request.user.pk)
	schadule = student.schadule
	current = student.current_scores
	max_current = student.current_max_scores
	absolute_max = student.absolute_max_scores
	return render(request, 'mainApp/brs.html', {'schadule': schadule, 'max_current': max_current,
												'current': current, 'absolute_max': absolute_max, })
