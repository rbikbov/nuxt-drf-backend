from django.conf.urls import url, include
from django.views.defaults import page_not_found
from django.views.generic import RedirectView, TemplateView

from .views import checkExists

urlpatterns = [
    # перехватываем доступ к URL, т.к. он не нужен
    url(r'^auth/registration/account-confirm-email/([-:\w]+)/$',
        RedirectView.as_view(url='/', permanent=True)),


    # чтобы не было ошибки при регистрации и попытке отправить письмо
    url(r'^confirm-email/$',
        RedirectView.as_view(url='/', permanent=True),
        name='account_email_verification_sent'),


    # url для генерации правильной ссылки в письме
    # на фронтенд страницу подтверждения сброса пароля
    url(r'^auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        RedirectView.as_view(url='/', permanent=True),
        name='password_reset_confirm'),

    # url для генерации правильной ссылки в письме
    # на фронтенд страницу подтверждения электронной почты
    url(r'^auth/registration/confirm-email/(?P<key>[-:\w]+)/$',
        RedirectView.as_view(url='/', permanent=True),
        name='account_confirm_email_frontend'),


    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^api/v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/auth/check/', checkExists),
]