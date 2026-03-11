from rest_framework import routers
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import  ProjectViewSet
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns = router.urls