from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import PostModelViewSet, UserModelViewSet
router = DefaultRouter()

router.register('posts', PostModelViewSet, 'posts')
router.register('users', UserModelViewSet, 'users')

urlpatterns = [
    path('', include(router.urls))
]