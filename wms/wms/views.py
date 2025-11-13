from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings

def login(request):
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/authorize"
        f"?audience={settings.AUTH0_AUDIENCE}"
        f"&response_type=code"
        f"&client_id={settings.AUTH0_CLIENT_ID}"
        f"&redirect_uri={settings.AUTH0_CALLBACK_URL}"
        f"&prompt=login" 
    )


def callback(request):
    return redirect(settings.LOGIN_REDIRECT_URL)

def logout(request):
    django_logout(request)
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout"
        f"?returnTo={settings.LOGOUT_REDIRECT_URL}"
        f"&client_id={settings.AUTH0_CLIENT_ID}" 
    )
