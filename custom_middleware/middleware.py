from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

from django.urls import reverse


def get_login_url():
    return reverse(settings.LOGIN_URL_NAME)


def get_exempts():
    exempts = [compile(get_login_url().lstrip('/'))]
    if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
        exempts += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]
    return exempts


class LoginRequiredMiddleware(object):
    """
        Middleware that requires a user to be authenticated to view any page other
        than reverse(LOGIN_URL_NAME). Exemptions to this requirement can optionally
        be specified in settings via a list of regular expressions in
        LOGIN_EXEMPT_URLS (which you can copy from your urls.py).
        
        Requires authentication middleware and template context processors to be
        loaded. You'll get an error if they aren't.
        """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
        requires authentication middleware to be installed. Edit your\
        MIDDLEWARE_CLASSES setting to insert\
        'django.contrib.auth.middlware.AuthenticationMiddleware'. If that\
        doesn't work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
        'django.core.context_processors.auth'."
        if not request.user.is_authenticated():
            path = request.path.lstrip('/')
            if not any(m.match(path) for m in get_exempts()):
                return HttpResponseRedirect(
                                            get_login_url() + "?next=" + request.path)
