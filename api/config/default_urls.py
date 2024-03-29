from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path


from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Frontend Serving
if settings.DEBUG:
    urlpatterns += static('/dist/', document_root=settings.FRONTEND_DIST_DIR)

urlpatterns += [
    re_path('', serve, kwargs={'path': 'index.html', 'document_root': settings.FRONTEND_DIST_DIR}, name='index')
]
