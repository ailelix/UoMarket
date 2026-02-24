from django.shortcuts import redirect
from django.http import JsonResponse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Define dirs that bypass the middleware
        whitelist = [
            '/login',
            '/logout',
            '/api/callback'
        ]

        path = request.path_info

        if path not in whitelist and not request.user.is_authenticated:
            # If it is API ask the frontend to redirect login
            if path.startswith('/api/'):
                return JsonResponse({'status': 'error', 'msg': 'User not logged in'}, status=401)

            # If it is page request just redirect to login page
            return redirect('/login')

        response = self.get_response(request)
        return response
