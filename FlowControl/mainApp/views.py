from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accountApp.models import Profile
from accountApp.models import Settings
from accountApp.models import Sidebar
# Create your views here.

def disk_page(request):
	if request.user.pk is not None:
		settings = Settings.objects.get(pk=request.user.pk)
		disk_url = settings.url_of_disk
		sidebar_items = Sidebar.objects.all()
		return render(request, 'mainApp/disk.html', {'disk_url': disk_url, 'sidebar_items': sidebar_items})

	return render(request, 'mainApp/disk.html')

def display_notes(request):
	if request.user.pk is not None:
		settings = Settings.objects.get(pk=request.user.pk)
		notes_url = settings.url_of_notes
		sidebar_items = Sidebar.objects.all()
		return render(request, 'mainApp/notes.html', {'notes_url': notes_url, 'sidebar_items': sidebar_items})

	return render(request, 'mainApp/notes.html')

@login_required
def brs_view(request):
	student = Profile.objects.get(pk=request.user.pk)
	schadule = student.schadule
	current = student.current_scores
	max_current = student.current_max_scores
	absolute_max = student.absolute_max_scores
	sidebar_items = Sidebar.objects.all()
	return render(request, 'mainApp/brs.html', {'schadule': schadule, 'max_current': max_current,
												'current': current, 'absolute_max': absolute_max, 'sidebar_items': sidebar_items})
