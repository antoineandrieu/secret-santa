from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ParticipantViewSet,
    BlacklistViewSet,
    DrawViewSet,
)

router = DefaultRouter()
router.register(r"participants", ParticipantViewSet)
router.register(r"blacklists", BlacklistViewSet)
router.register(r"draws", DrawViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
