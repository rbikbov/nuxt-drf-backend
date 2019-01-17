from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Redefined for correct link to frontend in the account confirmation
        email.
        """
        url = reverse(
            "account_confirm_email_frontend",
            args=[emailconfirmation.key])
        ret = build_absolute_uri(
            None,
            url)
        return ret
