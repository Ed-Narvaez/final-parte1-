"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experience'), namespace='experience')),
    path('', include(('autos.urls', 'autos'), namespace='autos')),
    path('', include(('tipo.urls', 'tipo'), namespace='tipo')),
    path('', include(('marca.urls', 'marca'), namespace='marca')),
    path('', include(('search.urls', 'search'), namespace='search')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
