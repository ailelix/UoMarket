from django.shortcuts import redirect
from django.http import JsonResponse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Define dirs that bypass the middleware
        whitelist = [
            '/login',
            '/api/login',
            '/api/logout',
            '/api/callback'
        ]

        path = request.path_info

        # Bypass static assets
        if path.startswith('/static/') or path.startswith('/assets/') or path.startswith('/media/') or path == '/favicon.ico':
            return self.get_response(request)

        if path not in whitelist and not request.user.is_authenticated:
            # If it is API ask the frontend to redirect login
            if path.startswith('/api/'):
                return JsonResponse({'status': 'error', 'msg': 'User not logged in'}, status=401)

            # If it is page request just let Vue handle the Auth state
            return self.get_response(request)

        response = self.get_response(request)
        return response
