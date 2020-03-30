from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup
from .models import Settings

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


def user_page(request):
    if request.user.pk is not None:
        student = Profile.objects.get(pk=request.user.pk)
        schadule_list = student.schadule.split('SEP')
        info = student.student_info
        if info == 'empty':
            info = 'Введите учетные данные ЛК ЮФУ, чтобы видеть подробную информацию.'
        return render(request, 'accountApp/user.html', {'schadule_list': schadule_list[1:], 'info': info})

    return render(request, 'accountApp/user.html')

@login_required()
def register_note_client(request, email='korzh@sfedu.ru', password='Vk#nF#RwA4.LpW2'):
    url_to_register = r'https://nimbusweb.me/auth?f=register&int_source=top_button_no_email'

    headers_to_register = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
        'origin': 'https://nimbusweb.me',
        'referer': 'https://nimbusweb.me/ru/',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
    }

    headers_to_form = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'NM_FIRST_CLICK=%7B%22first-click-referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22first-click-utm-source%22%3A%22nodata%22%2C%22first-click-utm-medium%22%3A%22direct%22%2C%22first-click-utm-campaign%22%3A%22%22%2C%22first-click-utm-term%22%3A%22%22%2C%22first-click-utm-content%22%3A%22%22%2C%22first-click-date%22%3A%222020-03-30+12%3A56%3A56%22%7D; eversessionid=11g64W17eq6p2B3VHxcoxIaZeHnN17kF; _ga=GA1.2.564419870.1585573020; _gid=GA1.2.1016265769.1585573020; NM_LAST_CLICK=%7B%22last-click-referer%22%3A%22%22%2C%22last-click-utm-source%22%3A%22nodata%22%2C%22last-click-utm-medium%22%3A%22direct%22%2C%22last-click-utm-campaign%22%3A%22%22%2C%22last-click-utm-term%22%3A%22%22%2C%22last-click-utm-content%22%3A%22%22%2C%22last-click-date%22%3A%222020-03-30+12%3A57%3A08%22%7D; _fbp=fb.1.1585573031765.416816130; _gat_gtag_UA_67774717_27=1; _gali=form_register',
        'origin': 'https://nimbusweb.me',
        'referer': 'https://nimbusweb.me/auth/?f=register&int_source=top_button_no_email',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-client-software': 'auth_form',
        'x-requested-with': 'XMLHttpRequest',
    }

    url_to_pass_form = r'https://nimbusweb.me/auth/api/register'
    payload = {"login": email, "password": password, "service": "nimbus", "subscribe": 'true'}
    with requests.Session() as s:
        responce_from_register_page = s.get(url_to_register, headers=headers_to_register)
        responce_from_post = s.post(url_to_pass_form, headers=headers_to_form, data=payload)

    return HttpResponse(responce_from_post)

@login_required()
def get_brs_info(request):

    user = request.user
    student_settings = Settings.objects.create(pk=user.pk)
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

    student_info_tags = list(soup.find('div', {'id': 'profileInfo'}))
    student_info = ''

    for tag in student_info_tags[1:]:
        student_info += tag.text + 'SEP'
    student.student_info = student_info
    student.student_name = soup.find('div', {'class': 'username'}).text
    student.scoreline = ''.join(brs_table.values())
    student.schadule = ''.join(brs_table.keys())
    student.save()
    return HttpResponseRedirect('/account/')

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
    if request.user.pk is not None:
        student = Profile.objects.get(pk=request.user.pk)
        schadule_list = student.schadule.split('SEP')
        if len(schadule_list) <= 1:
            return render(request, 'accountApp/edit.html', {'schadule_list': [],
                                                            'user_form': user_form, 'profile_form': profile_form})

        else:
            return render(request, 'accountApp/edit.html', {'schadule_list': schadule_list[1:],
                                                            'user_form': user_form, 'profile_form': profile_form})

    return render(request, 'accountApp/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
