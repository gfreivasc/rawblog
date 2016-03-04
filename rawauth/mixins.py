from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse


class RawLoginRequiredMixin(LoginRequiredMixin):
    """Centralized login hook for required pages"""

    def get_login_url(self):
        return reverse('rawauth:login')
