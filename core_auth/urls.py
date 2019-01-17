from django.conf.urls import url, include
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
    # intercepts access to the URL, because it is not needed
    url(r'^auth/registration/account-confirm-email/([-:\w]+)/$',
        RedirectView.as_view(url='/', permanent=True)),


    # so that there is no error when registering and trying to send an email
    url(r'^confirm-email/$',
        RedirectView.as_view(url='/', permanent=True),
        name='account_email_verification_sent'),


    # url to generate the correct link in the email
    # to the frontend password reset confirmation page
    url(r'^auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        RedirectView.as_view(url='/', permanent=True),
        name='password_reset_confirm'),

    # url to generate the correct link in the email
    # to the frontend email confirmation page
    url(r'^auth/registration/confirm-email/(?P<key>[-:\w]+)/$',
        RedirectView.as_view(url='/', permanent=True),
        name='account_confirm_email_frontend'),

    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^api/v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/auth/check/', views.checkExists),
]
