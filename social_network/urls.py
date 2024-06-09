from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from direct.views import DirectMessageViewSet
from board.views import BoardMessageViewSet,BoardViewSet
from logs.views import UserLogViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'direct', DirectMessageViewSet, basename='dm')
router.register(r'board_message', BoardMessageViewSet, basename='chat')
router.register(r'board', BoardViewSet, basename='chatroom')
router.register(r'logs', UserLogViewSet, basename='log')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('users.urls')),
    path('auth/', ObtainAuthToken.as_view()),
]
