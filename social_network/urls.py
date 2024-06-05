from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from direct.views import DirectMessageViewSet
from board.views import BoardMessageViewSet
from logs.views import UserLogViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'direct', DirectMessageViewSet, basename='dm')
router.register(r'board', BoardMessageViewSet, basename='chat')
router.register(r'logs', UserLogViewSet, basename='log')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('users.urls')),
    path('auth/', ObtainAuthToken.as_view()),
]
