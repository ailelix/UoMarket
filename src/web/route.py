from django.urls import path, re_path
from . import view

routes = [
    # Define APIs first
    path('/login', view.uom_login_start),
    path('/api/callback', view.uom_auth_callback),

    # Route common pages to Vue actual sites
    re_path(r'^.*$', view.index)
]


