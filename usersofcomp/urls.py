from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet

router = DefaultRouter()

router.register('', CompanyViewSet)

urlpatterns = [
    path('<int>id/', CompanyViewSet.as_view({'put': 'retrieve'})),
] + router.urls
