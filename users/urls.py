from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, active

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('active/', active, name='active_users'),
    path('', include(router.urls)),
]
