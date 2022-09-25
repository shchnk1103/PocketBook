from django.urls import path, include
from rest_framework import routers

from .views import PocketBookViewSet

router = routers.DefaultRouter()
router.register(r'pocketbooks', PocketBookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
