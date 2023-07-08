from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from user.views import UserViewSet, GroupViewSet

from playvie.views import handler404


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/movies/', include('movie.urls')),
    path('api/v1/playlists/', include('playlist.urls'))
]

handler500 = 'rest_framework.exceptions.server_error'
handler404 = handler404