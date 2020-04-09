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
		sidebar_items = request.user.profile.sidebar_set.all()
		return render(request, 'mainApp/disk.html', {'disk_url': disk_url, 'sidebar_items': sidebar_items})

	return render(request, 'mainApp/disk.html')

@login_required
def display_notes(request):

	settings = request.user.settings
	notes_url = settings.url_of_notes
	sidebar_items = request.user.profile.sidebar_set.all()
	url = str(request.get_full_path())
	start_index =url.find('link=') + len('link=')
	item_name ='Заметки'
	if start_index != len('link=') -1:
		url = url[start_index:]
		if url == notes_url:
			item_name = 'Заметки'
		else:

			try:
				item = request.user.profile.sidebar_set.get(homework_link=url)
				item_name = item.name
				notes_url = url
				print('here', notes_url)
			except Sidebar.DoesNotExist:
				item_name = 'Заметки'
			# except Sidebar.MultipleObjectsReturned:
			# 	item_name = 'Заметки'
			# 	notes_url = url

			try:
				item = request.user.profile.sidebar_set.get(aims_link=url)
				item_name = item.name
				notes_url = url
				print('here', notes_url)
			except Sidebar.DoesNotExist:
				pass
			# except Sidebar.MultipleObjectsReturned:
			# 	item_name = 'Заметки'
			# 	notes_url = url

			try:
				item = request.user.profile.sidebar_set.get(todo_link=url)
				item_name = item.name
				notes_url = url
				print('here', notes_url)
			except Sidebar.DoesNotExist:
				pass
			# except Sidebar.MultipleObjectsReturned:
			# 	item_name = 'Заметки'
			# 	notes_url = url



	return render(request, 'mainApp/notes.html', {'notes_url': notes_url, 'item_name': item_name,
													  'sidebar_items': sidebar_items})

@login_required
def brs_view(request):
	student = request.user.profile
	schadule = student.schadule
	current = student.current_scores
	max_current = student.current_max_scores
	absolute_max = student.absolute_max_scores
	sidebar_items = student.sidebar_set.all()
	return render(request, 'mainApp/brs.html', {'schadule': schadule, 'max_current': max_current,
												'current': current, 'absolute_max': absolute_max, 'sidebar_items': sidebar_items})
def reference_view(request):
	if request.user.is_authenticated:
		sidebar_items = request.user.profile.sidebar_set.all()
		return render(request, 'mainApp/help.html', {'sidebar_items': sidebar_items})
	else:
		return render(request, 'mainApp/help.html', {'sidebar_items': []})