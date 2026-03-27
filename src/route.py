from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve
import os
from . import view

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    # Serve Vite assets folder
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'frontend', 'dist', 'assets')}),
    
    # Define APIs first
    path('api/login', view.uom_login_start),
    path('api/callback', view.uom_auth_callback),
    path('api/me', view.get_me),
    path('api/logout', view.uom_logout),
    
    path('api/items', view.handle_items_api),
    path('api/items/<int:item_id>', view.handle_single_item_api),
    path('api/bids', view.post_bid),
    path('api/users/<int:user_id>', view.get_user),
    path('api/category/<int:category_id>', view.get_category),
    path('api/categorys', view.get_categories),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Route common pages to Vue actual sites
urlpatterns += [
    re_path(r'^.*$', view.index)
]
