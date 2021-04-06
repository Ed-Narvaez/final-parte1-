"""Education URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from education import views

router = DefaultRouter()
router.register(r'autos', views.EducationViewSet, basename='autos')

urlpatterns = [
    path('', include(router.urls))
]