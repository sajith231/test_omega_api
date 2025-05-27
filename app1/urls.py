from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccAdvancesViewSet

router = DefaultRouter()
router.register(r'acc_advances', AccAdvancesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
