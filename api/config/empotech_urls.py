from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from django.views.static import serve


urlpatterns = []

# Frontend Serving
if settings.DEBUG:
    urlpatterns += static('/dist/', document_root=settings.EMPOTECH_DIST_DIR)

urlpatterns += [
    path('', serve, kwargs={'path': 'index.html', 'document_root': settings.EMPOTECH_DIST_DIR}, name='index')
]
