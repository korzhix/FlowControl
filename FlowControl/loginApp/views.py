from django.shortcuts import render
from django.http import HttpResponse
from .models import SfeduStuden
from .forms import LoginForm


# Create your views here.
#  def login_page(request):
#  	return render(request, 'mainApp/login.html')
#
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            SfeduStuden.sfedu_username=cd['username']
            SfeduStuden.sfedu_pass = cd['password']

        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'loginApp/login.html', {'form': form})
# # def user_login(request):
# #     if request.method == 'POST':
# #         form = LoginForm(request.POST)
# #         if form.is_valid():
# #             cd = form.cleaned_data
# #             user = authenticate(username=cd['username'], password=cd['password'])
# #             if user is not None:
# #                 if user.is_active:
# #                     login(request, user)
# #                     render(request, 'mainApp/login.html',)
# #                 else:
# #                     render(request, 'mainApp/login.html', {'form': form})
# #             else:
# #                 render(request, 'mainApp/login.html', {'form': form})
# #     else:
# #         form = LoginForm()
# #     return render(request, 'mainApp/login.html', {'form': form})