from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .forms import ProfileForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup


class RegisterFormView(FormView):
    # form_class = UserCreationForm
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "accountApp/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "accountApp/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def user_login(request):
    return render(request, 'accountApp/user.html')

@login_required()
def get_brs_info(request):

    user = request.user
    student = Profile.objects.get(pk=user.pk)
    payload_to_login = {'openid_url': student.sfedu_username, 'password': student.sfedu_pass}

    headers_to_login = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '40',
        'Content-Type': 'application/x-www-form-urlencoded',

        'Origin': 'https://openid.sfedu.ru',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    }

    login_url = r'https://openid.sfedu.ru/server.php/login'
    url_from_brs_to_openid = r'https://grade.sfedu.ru/handler/sign/openidlogin?loginopenid=' + str(student.sfedu_username) + '@sfedu.ru&user_role=student'

    headers_from_brs_to_openid = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://grade.sfedu.ru',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }

    with requests.Session() as s:

        responce_from_brs_to_login = s.get(url_from_brs_to_openid, headers=headers_from_brs_to_openid)
        headers_to_login['Referer'] = responce_from_brs_to_login.url
        login_responce = s.post(login_url, headers=headers_to_login, data=payload_to_login)

    brs_table = {}
    soup = BeautifulSoup(login_responce.content, 'html.parser')
    disc_tag_list = soup.findAll('td', {'class': 'discTitle'})
    score_tag_list = soup.findAll('td', {'class': 'discRating'})
    small_sep = 'sep'
    big_SEP = 'SEP'
    score_line = small_sep

    for i in range(1, len(score_tag_list) + 1):
        key = big_SEP + disc_tag_list[i].find('a').text

        spans = score_tag_list[i - 1].findAll('span')
        for j in range(len(spans)):
            score_line += spans[j].text + small_sep
        brs_table[key] = score_line
        score_line = ''

    if brs_table == {}:
        return HttpResponse('Для синхронизации с БРС необходимо заполнить учетные данные SFEDU')

    student.student_name = soup.find('div', {'class': 'username'}).text
    student.scoreline = ''.join(brs_table.values())
    student.schadule = ''.join(brs_table.keys())
    return HttpResponse(student.schadule + ' ' + student.scoreline + 'asd'+student.student_name)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accountApp/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
