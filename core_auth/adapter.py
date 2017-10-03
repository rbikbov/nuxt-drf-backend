from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.urls import reverse


class CustomDefaultAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = reverse(
            "account_confirm_email_frontend",
            args=[emailconfirmation.key])
        ret = build_absolute_uri(None, url)
        # ret = build_absolute_uri(request, url)
        return ret
