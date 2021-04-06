"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from marca import views

router = DefaultRouter()
router.register(r'marca', views.ExtraViewSet, basename='marca')

urlpatterns = [
    path('', include(router.urls))
]