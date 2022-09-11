from django.urls import path, include
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

from my_user.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'-api', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
