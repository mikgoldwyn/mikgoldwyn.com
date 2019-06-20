from django.urls import include, path
from rest_framework.routers import DefaultRouter


from . import views
from . import viewsets


router = DefaultRouter()
router.register(r'user', viewsets.UserViewset, base_name='user')

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
