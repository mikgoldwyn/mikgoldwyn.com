from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path


from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Frontend Serving
urlpatterns += [re_path('', serve, kwargs={'path': 'index.html', 'document_root': settings.DIST_DIR}, name='index')]
