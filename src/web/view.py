import requests
import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, get_user_model

User = get_user_model()

def index(request):
    return render(request, 'index.html')

def uom_login_start(request):
    cs_ticket = uuid.uuid4().hex
    request.session['cs_ticket'] = cs_ticket

    callback_url = request.build_absolute_uri('/api/callback')

    uom_auth_url = (
        f"https://studentnet.cs.manchester.ac.uk/authenticate/?"
        f"url={callback_url}&csticket={cs_ticket}&version=3&command=validate"
    )

    return redirect(uom_auth_url)

def uom_auth_callback(request):
    username = request.GET.get('username')
    fullname = request.GET.get('fullname')
    ticket_res = request.GET.get('csticket')

    ticket_session = request.session.get('cs_ticket')
    if not ticket_session or ticket_res != ticket_session:
        return HttpResponseBadRequest('Invalid session cookie')

    callback_url = request.build_absolute_uri('/api/callback')

    confirm_url = (
        f"https://studentnet.cs.manchester.ac.uk/authenticate/?"
        f"url={callback_url}&csticket={ticket_session}"
        f"&version=3&command=confirm&username={username}&fullname={fullname}"
    )

    response = requests.get(confirm_url)

    if response.status_code == 200:
        user, created = User.objects.get_or_create(username=username, defaults={"fullname": fullname})
        # Execute Django login
        login(request, user)
        return redirect('/')
    else:
        return HttpResponseBadRequest('Auth failed during confirmation')
