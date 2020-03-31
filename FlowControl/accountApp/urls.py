from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('edit.html', views.update_profile),
    re_path('logout.html', views.LogoutView.as_view()),
    re_path("login.html", views.LoginFormView.as_view()),
    re_path('register.html', views.RegisterFormView.as_view()),
    re_path(r'', views.user_login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)