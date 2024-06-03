from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from direct.views import DirectMessageViewSet
from board.views import BoardMessageViewSet
from logs.views import UserLogViewSet

router = DefaultRouter()
router.register(r'direct', DirectMessageViewSet)
router.register(r'board', BoardMessageViewSet)
router.register(r'logs', UserLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('users.urls')),
    path('auth/', include('rest_authtoken.urls')),
]